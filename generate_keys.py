from imports import *
Path('shared/keys').mkdir(parents=True ,exist_ok=True)
receiver_key=ECC.generate(curve='P-256')
private_pem= receiver_key.export_key(format='PEM')
public_pem=receiver_key.public_key().export_key(format='PEM')
Path('shared/keys/private_key.pem').write_text(private_pem)
Path('shared/keys/public_key.pem').write_text(public_pem)


print("keys generated successfully")