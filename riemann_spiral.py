import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
from scipy.constants import golden

# === Constants ===
PHI = golden
ALPHA_INV = 137.035999
# First few imaginary parts of non-trivial zeta zeros
ZETA_ZEROS = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

def get_spiral_coords(n):
    """
    Calculate polar coordinates based on the document:
    r(n) = 3 * sqrt(n)
    theta(n) = n * phi
    """
    r = 3 * np.sqrt(n)
    theta = n * PHI
    return r, theta

def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def visualize_riemann_spiral(num_points=500):
    """
    Visualizes the Riemann-Spiral Field Theory.
    """
    n_values = np.arange(1, num_points + 1)
    r_values, theta_values = get_spiral_coords(n_values)
    x_values, y_values = polar_to_cartesian(r_values, theta_values)

    plt.figure(figsize=(12, 12), facecolor='black')
    ax = plt.subplot(111, projection='polar')
    ax.set_facecolor('black')
    
    # Plot the spiral points
    # Color them based on a cyclic function to show the "flow"
    colors = plt.cm.viridis(np.linspace(0, 1, num_points))
    ax.scatter(theta_values, r_values, c=colors, s=10, alpha=0.6, label='Golden Spiral Nodes')

    # Highlight Zeta Zero resonant points (conceptual mapping)
    # The document suggests a mapping n <-> gamma_n. 
    # We'll mark the first few points corresponding to the integer indices of the zeros 
    # (or just the first N points to show the concept, as direct mapping n=gamma is not 1:1 integers usually)
    # For visualization, let's highlight points where n is close to a zeta zero value (if we treat n as continuous)
    # or just the first 10 points to represent the "embedded" zeros.
    
    # Let's highlight specific indices that might "resonate" (just first 10 for now as placeholders for the theory)
    resonant_indices = np.array([int(z) for z in ZETA_ZEROS]) # Simple integer casting for visualization
    res_r, res_theta = get_spiral_coords(resonant_indices)
    ax.scatter(res_theta, res_r, c='red', s=50, marker='x', label='Zeta Zero Resonances (Approx)')

    # Connect points to show the spiral arm structure
    # Since it's a discrete spiral, connecting sequential n can be messy, 
    # but let's try to show the "arms" by connecting points with similar phases if possible.
    # For now, just the scatter is cleaner.

    ax.set_title("Riemann-Spiral Field Theory Visualization", color='white', fontsize=16)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', alpha=0.3)
    
    plt.legend(loc='upper right')
    
    output_file = 'riemann_spiral_visualization.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"[OK] Visualization saved to {output_file}")

if __name__ == "__main__":
    visualize_riemann_spiral(num_points=1000)
