import numpy as np
import skfuzzy as fuzz
from PIL import Image
import matplotlib.pyplot as plt
import colorsys

image_path = 'brain.jpg'  
img = np.array(Image.open(image_path).convert('RGB')) 


height, width, channels = img.shape
pixels = img.reshape(-1, channels).astype(float)  


n_clusters = 3  
m = 2  
error = 0.005  
maxiter = 1000  
init = None  


centers, u, u0, d, jm, p, fpc = fuzz.cmeans(
    data=pixels.T, c=n_clusters, m=m, error=error, maxiter=maxiter, init=init
)


labels = np.argmax(u, axis=0)  

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


Image.fromarray(segmented_img.astype(np.uint8)).save('segmented_image.jpg')


fig, axes = plt.subplots(2, n_clusters + 1, figsize=(5 * (n_clusters + 1), 10))


axes[0, 0].imshow(img)
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')


axes[1, 0].imshow(segmented_img)
axes[1, 0].set_title('Segmented Image')
axes[1, 0].axis('off')


for i in range(n_clusters):

    membership_map = u[i, :].reshape(height, width)

    membership_img = (membership_map * 255).astype(np.uint8)
    Image.fromarray(membership_img).save(f'membership_cluster_{i}.jpg')

    axes[0, i + 1].imshow(membership_map, cmap='viridis')
    axes[0, i + 1].set_title(f'Membership Cluster {i}')
    axes[0, i + 1].axis('off')

    color_patch = np.ones((height // 10, width // 10, 3)) * np.array(colors[i]) / 255
    axes[1, i + 1].imshow(color_patch)
    axes[1, i + 1].set_title(f'Color for Cluster {i}')
    axes[1, i + 1].axis('off')

plt.tight_layout()
plt.savefig('fcm_results.png')
plt.close()