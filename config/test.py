This code 

```
def send_payment_tx(self,address,erg_value = 0.001, assets = []):
    erg_value = erg_value*10**9 
    send_payment_header = [ 
        { 
        'address': address, 
        'value': erg_value, 
        'assets': assets 
        }
        ]
    send_payment = requests.post(f"{self.req_url}wallet/payment/send", headers self.header, data json.dumps (send_payment_header)).json() 
    return send_payment
```

Is producing this error:

Every output of the transaction should contain at least <minValuePerByte * outputSize> nanoErgs.

didn t have any problems with it beforehand. It works with some transactions, and others get this error

the only difference that comes to mind is that i minted through that address and issued 100 more inputBoxes for royalties. Could that be the cause ?


