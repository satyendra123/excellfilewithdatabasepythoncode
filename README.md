# excellfilewithdatabasepythoncode
i have 70000 data in my excell file and this file will be uploaded in the database using python code

actually in the mohali project we have database in which we stored the data from the excell file in the database like qr code and the barcode. so what we have done is we have write the code in python which stores the data into the database from the excell. and the data will be like 70000, 60000. and all these data will be stored in the database at once only.




matchanddeactive.py wala jo code hai usme to simply hume ek excell files milegi blacklist wala. so usme agr barcode hai jo database me bhi hai aur uska status active hai to use hume deactive karna hai. so is code me humne excell se barcode uthaya aur iske bad database se barcode uthaya aur phir barcode ko match karaya one by one. aur agar barcode match ho gaya to uska status read kiya jayega aur agar uska status active hai to usko deactive kar denge. aur humne jo active se deactive ho jate hai hum uska date time bhi update kara dete hai taki hume suvidha ho ye check karne me ki kitne data hai jo abhi blacklist kiye gaye hai. so uske liye hum database me query likhege database me jo count karke btayega ki is date me sector code 90 ke kitne data hai jo deactive hue hai. aur hum same chiz ko apne excell se match kara lenge taki koi mistakes na hui ho
SELECT count(*) FROM `accreditation_card` WHERE sector = '90' AND status = 'Deactive' AND Created_at >= '2024-04-09 00:00:00' AND Created_at < '2024-04-10 00:00:00';
