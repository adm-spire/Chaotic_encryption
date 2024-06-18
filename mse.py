import numpy as np
import matplotlib.pyplot as plt
import cv2

def mse(image1, image2):
    """Calculate the Mean Squared Error (MSE) between two images."""
    return np.mean((image1 - image2) ** 2)

def psnr(original_image, encrypted_image,mse):
    
    # Convert the pixel values to float64
    original_image = original_image.astype(np.float64)
    encrypted_image = encrypted_image.astype(np.float64)
    
    
    
    # Calculate the maximum possible pixel value
    max_pixel_value = 255.0  # For grayscale images
    
    # Calculate PSNR using the formula: PSNR = 20 * log10(MAX) - 10 * log10(MSE)
    psnr_value = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    
    return psnr_value

# Load the original grayscale image
original_image = plt.imread("cameraman.bmp")

# Load the encrypted grayscale image
encrypted_image = cv2.imread("DecryptedImage.bmp", cv2.IMREAD_GRAYSCALE)



# Check the dimensions of the original image
if len(original_image.shape) == 3:
    height, width, channels = original_image.shape
else:
    height, width = original_image.shape
    channels = 1  # Grayscale image has only one channel

print("Original Image shape (height, width, channels):", height, width, channels)

# Check the dimensions of the encrypted image
if len(encrypted_image.shape) == 3:
    height_enc, width_enc, channels_enc = encrypted_image.shape
else:
    height_enc, width_enc = encrypted_image.shape
    channels_enc = 1  # Grayscale image has only one channel

print("Encrypted Image shape (height, width, channels):", height_enc, width_enc, channels_enc)

# Ensure that both images have the same shape
if (height, width, channels) != (height_enc, width_enc, channels_enc):
    raise ValueError("The shapes of the original and encrypted images must match.")

# Calculate the Mean Squared Error (MSE)
mse_value = mse(original_image, encrypted_image)
print("Mean Squared Error (MSE) between original and encrypted images:", mse_value)
psnr_value = psnr(original_image,encrypted_image,mse_value)
print("psnr value:",psnr_value)
# Display the original and encrypted images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(encrypted_image, cmap='gray')
plt.title('Encrypted Image')
plt.axis('off')

plt.show()

