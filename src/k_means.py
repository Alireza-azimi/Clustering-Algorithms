import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import colorsys


image_path = 'brain.jpg'  
img = np.array(Image.open(image_path).convert('RGB')) 


height, width, channels = img.shape
pixels = img.reshape(-1, channels).astype(float)  


n_clusters = 3  
random_state = 0  


kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
kmeans.fit(pixels)
labels = kmeans.labels_ 


def get_distinct_colors(n):
    hsv_colors = [(i / n, 1.0, 1.0) for i in range(n)]  
    rgb_colors = [colorsys.hsv_to_rgb(h, s, v) for h, s, v in hsv_colors]
    rgb_colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in rgb_colors]
    return rgb_colors

colors = get_distinct_colors(n_clusters)


segmented_img = np.zeros_like(img)
for i in range(n_clusters):
    mask = labels.reshape(height, width) == i
    segmented_img[mask] = colors[i]


Image.fromarray(segmented_img.astype(np.uint8)).save('segmented_image_kmeans.jpg')


fig, axes = plt.subplots(1, 2, figsize=(10, 5))


axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')


axes[1].imshow(segmented_img)
axes[1].set_title('Segmented Image (K-Means)')
axes[1].axis('off')

plt.tight_layout()
plt.savefig('kmeans_results.png')
plt.close()