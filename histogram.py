import numpy as np
import matplotlib.pyplot as plt

# Load the original and encrypted images
original_image = plt.imread("cameraman.bmp")
encrypted_image = plt.imread("EncryptedImage.bmp")

# Flatten the images to 1D arrays
original_flat = original_image.flatten()
encrypted_flat = encrypted_image.flatten()

# Plot histograms
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(original_flat, bins=256, color='blue', alpha=0.7)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(encrypted_flat, bins=256, color='red', alpha=0.7)
plt.title('Histogram of Encrypted Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
