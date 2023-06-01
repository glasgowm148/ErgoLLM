import os
import re
import openai
import discord
import emojis
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from discord.ext import commands

import unicodedata

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(DISCORD_BOT_TOKEN)
print(OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

YOUTUBE_URL_REGEX = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"

LANGUAGE_MAP = {
    'us': 'English',
    'gb': 'English',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'it': 'Italian',
    'jp': 'Japanese',
    'kr': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ar': 'Arabic',
    'cn': 'Chinese',
    'tr': 'Turkish',
    'pl': 'Polish',
    'nl': 'Dutch',
    'id': 'Indonesian',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'sv': 'Swedish',
    'no': 'Norwegian',
    'da': 'Danish',
    'fi': 'Finnish',
    'el': 'Greek',
    'ro': 'Romanian',
    'hu': 'Hungarian',
    'cs': 'Czech',
    'hi': 'Hindi'
}

def get_channel_language(channel_name):
    # Extract the language from the flag emoji in the channel name, if present
    for c in channel_name:
        if unicodedata.name(c).startswith('REGIONAL INDICATOR SYMBOL LETTER'):
            flag_letters = [unicodedata.name(c).split()[-1] for c in channel_name if unicodedata.name(c).startswith('REGIONAL INDICATOR SYMBOL LETTER')]
            flag = ''.join(flag_letters).lower()
            return LANGUAGE_MAP.get(flag, flag.title())  # Look up the language name for the country code or use the capitalized country code as a fallback
    return 'English'  # If no flag emoji is present, use English as the default language




async def generate_summary(transcript, language):
    print(language)
    transcript = re.sub(r'\[.*?\]', '', transcript)
    prompt = f"Please generate a high level bullet point summary of the following YouTube video transcript in simple terms:\n\n{transcript}"
    if language != 'en':
        prompt += f"\n\nConvert it into {language} and provide it as a high level summarised bullet point list"
    print("PROMPT:")
    print(prompt)
    prompt_tokens = len(prompt.split())
    max_tokens = min(2000, prompt_tokens + 500)
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    print(response)
    summary = response.choices[0].text.strip()
    return summary

def get_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([t['text'] for t in transcript_data])
        return transcript
    except NoTranscriptFound:
        return None




def get_channel_language(channel_name):
    # Extract the language from the flag emoji in the channel name, if present
    for c in channel_name:
        if unicodedata.name(c).startswith('REGIONAL INDICATOR SYMBOL LETTER'):
            flag_letters = [unicodedata.name(c).split()[-1] for c in channel_name if unicodedata.name(c).startswith('REGIONAL INDICATOR SYMBOL LETTER')]
            flag = ''.join(flag_letters).lower()
            return LANGUAGE_MAP.get(flag, flag.title())  # Look up the language name for the country code or use the capitalized country code as a fallback
    return 'English'  # If no flag emoji is present, use English as the default language

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel_language = get_channel_language(message.channel.name)

    youtube_url_match = re.search(YOUTUBE_URL_REGEX, message.content)
    if youtube_url_match:
        video_id = youtube_url_match.group(6)
        transcript = get_transcript(video_id)
        if transcript:
            summary = await generate_summary(transcript, language=channel_language)
            if summary:
                await message.channel.send(f"Summary of the video:\n{summary}")

    await client.process_commands(message)
@client.command()
async def ask(ctx, *, question: str):
    answer = await ask_chatgpt(question)
    await ctx.send(answer)

client.run(DISCORD_BOT_TOKEN)