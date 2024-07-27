# Chaotic_encryption
### Encrypting an image by converting it to text data and then running conventional algorithms might can be a complex task , this project aims at utilising a simple method of image encryption 
### Image pixels are shuffled at sender's side using chaotic maps and keys are shared using ECC algorithm.

> [!IMPORTANT]
> ## Usage
> - keygenerator.py is the main function which is performing encryption , in my code i have used logistic map , which is the simplest chaotic map.
>   - Users can use different maps and combinations as per their needs
> - encryption.py is the main program which shuffles pixels according to the keys generated by the chaotic map and also decrypts it
> - ecc.py generates keys for sharing and ecc_decrypt.py decrypts it.
> - mse.py and correlation.py are meant for correlation and mse tests.

> [!NOTE]
> - This project is meant for demonstration of concept , to use it for practical purposes some modifications are needed.

![](The-original-cameraman-image.png)
![](EncryptedImage.bmp)



