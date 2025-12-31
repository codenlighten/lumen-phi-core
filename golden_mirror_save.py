"""
Golden Ratio Mirroring Visualization - Save to Files
Demonstrates how two golden spirals mirror vertically and horizontally to create a connected field
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection

# Golden ratio
PHI = (1 + np.sqrt(5)) / 2

def golden_spiral(theta_max=6*np.pi, points=1000):
    """
    Generate points for a golden spiral using polar coordinates.
    r = a * phi^(2*theta/pi)
    """
    theta = np.linspace(0, theta_max, points)
    # Scale factor chosen to make visualization cleaner
    a = 0.1
    r = a * np.power(PHI, 2*theta/np.pi)
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y, theta, r

def mirror_vertical(x, y):
    """Mirror points across horizontal axis (flip vertically)"""
    return x, -y

def mirror_horizontal(x, y):
    """Mirror points across vertical axis (flip horizontally)"""
    return -x, y

def create_2d_visualization():
    """Create 2D visualization showing the mirroring progression"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Golden Spiral Mirroring: The Connection Point', fontsize=16, fontweight='bold')
    
    # Generate original spiral
    x, y, theta, r = golden_spiral(theta_max=5*np.pi, points=1000)
    
    # 1. Original spiral
    ax = axes[0, 0]
    ax.plot(x, y, 'b-', linewidth=2, label='Original')
    ax.plot(0, 0, 'ro', markersize=8, label='Center')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('1. Original Golden Spiral', fontsize=12, fontweight='bold')
    ax.legend()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    
    # 2. Vertical mirror (creates heart/apple shape)
    ax = axes[0, 1]
    x_mirror_v, y_mirror_v = mirror_vertical(x, y)
    ax.plot(x, y, 'b-', linewidth=2, label='Original')
    ax.plot(x_mirror_v, y_mirror_v, 'r-', linewidth=2, label='Vertical Mirror')
    ax.plot(0, 0, 'ko', markersize=8, label='Connection Point')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2. Vertical Mirror → "Heart" Shape', fontsize=12, fontweight='bold')
    ax.legend()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    
    # 3. Full 4-fold symmetry
    ax = axes[0, 2]
    x_mirror_v, y_mirror_v = mirror_vertical(x, y)
    x_mirror_h, y_mirror_h = mirror_horizontal(x, y)
    x_mirror_both, y_mirror_both = mirror_horizontal(x_mirror_v, y_mirror_v)
    
    ax.plot(x, y, 'b-', linewidth=2, label='Q1: Original')
    ax.plot(x_mirror_v, y_mirror_v, 'r-', linewidth=2, label='Q4: V-Mirror')
    ax.plot(x_mirror_h, y_mirror_h, 'g-', linewidth=2, label='Q2: H-Mirror')
    ax.plot(x_mirror_both, y_mirror_both, 'm-', linewidth=2, label='Q3: Both')
    ax.plot(0, 0, 'ko', markersize=10, label='Singularity')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('3. Full 4-Fold Symmetry → Magnetic Field', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    
    # 4. Zoomed view showing connection at center
    ax = axes[1, 0]
    ax.plot(x, y, 'b-', linewidth=3)
    ax.plot(x_mirror_v, y_mirror_v, 'r-', linewidth=3)
    ax.plot(x_mirror_h, y_mirror_h, 'g-', linewidth=3)
    ax.plot(x_mirror_both, y_mirror_both, 'm-', linewidth=3)
    ax.plot(0, 0, 'ko', markersize=12)
    
    # Add arrows showing flow toward center
    ax.annotate('', xy=(0, 0), xytext=(2, 2),
                arrowprops=dict(arrowstyle='->', lw=2, color='blue', alpha=0.5))
    ax.annotate('', xy=(0, 0), xytext=(2, -2),
                arrowprops=dict(arrowstyle='->', lw=2, color='red', alpha=0.5))
    ax.annotate('', xy=(0, 0), xytext=(-2, 2),
                arrowprops=dict(arrowstyle='->', lw=2, color='green', alpha=0.5))
    ax.annotate('', xy=(0, 0), xytext=(-2, -2),
                arrowprops=dict(arrowstyle='->', lw=2, color='magenta', alpha=0.5))
    
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('4. Zoomed: Connection at Center', fontsize=12, fontweight='bold')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.text(0, -4, 'All spirals converge to (0,0)\n∞ self-similarity', 
            ha='center', fontsize=10, style='italic')
    
    # 5. Tangent continuity visualization
    ax = axes[1, 1]
    # Show how tangent angles match at boundaries
    sample_points = [100, 200, 300, 400, 500]
    colors = plt.cm.viridis(np.linspace(0, 1, len(sample_points)))
    
    ax.plot(x, y, 'b-', linewidth=2, alpha=0.5)
    ax.plot(x_mirror_v, y_mirror_v, 'r-', linewidth=2, alpha=0.5)
    
    for idx, i in enumerate(sample_points):
        # Calculate tangent vectors
        if i < len(x) - 1:
            dx = x[i+1] - x[i]
            dy = y[i+1] - y[i]
            # Draw tangent line
            scale = 2
            ax.arrow(x[i], y[i], dx*scale, dy*scale, 
                    head_width=0.3, head_length=0.2, fc=colors[idx], ec=colors[idx])
            
            # Mirror tangent
            dx_m, dy_m = dx, -dy
            ax.arrow(x[i], -y[i], dx_m*scale, dy_m*scale, 
                    head_width=0.3, head_length=0.2, fc=colors[idx], ec=colors[idx], alpha=0.7)
    
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('5. Tangent Continuity at Boundaries', fontsize=12, fontweight='bold')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.text(0, -13, f'φ = {PHI:.6f}\nSelf-similar growth', 
            ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # 6. Field line interpretation (like magnetic field)
    ax = axes[1, 2]
    # Create denser spiral for field effect
    x_dense, y_dense, _, _ = golden_spiral(theta_max=5*np.pi, points=2000)
    
    # Plot all four quadrants with gradient color
    for spiral_x, spiral_y, color, label in [
        (x_dense, y_dense, 'blue', 'Q1'),
        (x_dense, -y_dense, 'red', 'Q4'),
        (-x_dense, y_dense, 'green', 'Q2'),
        (-x_dense, -y_dense, 'magenta', 'Q3')
    ]:
        # Color gradient along the spiral
        points = np.array([spiral_x, spiral_y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        
        lc = LineCollection(segments, cmap='cool', linewidth=2)
        lc.set_array(np.linspace(0, 1, len(spiral_x)))
        ax.add_collection(lc)
    
    ax.plot(0, 0, 'yo', markersize=15, label='Singularity')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('6. Toroidal Field Pattern', fontsize=12, fontweight='bold')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.text(0, 13, 'Vortex Cross-Section', ha='center', fontsize=10, 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    return fig

def create_3d_visualization():
    """Create 3D visualization showing toroidal/vortex interpretation"""
    fig = plt.figure(figsize=(16, 8))
    
    # 3D vortex interpretation
    ax1 = fig.add_subplot(121, projection='3d')
    
    # Generate spiral in 3D (treating it as a vortex flowing along z-axis)
    x, y, theta, r = golden_spiral(theta_max=5*np.pi, points=1000)
    z = np.linspace(0, 10, len(x))
    
    # Four spirals
    ax1.plot(x, y, z, 'b-', linewidth=2, label='Spiral 1')
    ax1.plot(x, -y, z, 'r-', linewidth=2, label='Spiral 2')
    ax1.plot(-x, y, z, 'g-', linewidth=2, label='Spiral 3')
    ax1.plot(-x, -y, z, 'm-', linewidth=2, label='Spiral 4')
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z (flow direction)')
    ax1.set_title('3D Vortex Flow Pattern', fontsize=14, fontweight='bold')
    ax1.legend()
    
    # Torus approximation
    ax2 = fig.add_subplot(122, projection='3d')
    
    # Create a torus-like structure using the golden spiral
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, 2*np.pi, 50)
    U, V = np.meshgrid(u, v)
    
    # Major and minor radii following golden ratio
    R = PHI * 2  # Major radius
    r_minor = 2 / PHI  # Minor radius (reciprocal relationship)
    
    X = (R + r_minor * np.cos(V)) * np.cos(U)
    Y = (R + r_minor * np.cos(V)) * np.sin(U)
    Z = r_minor * np.sin(V)
    
    ax2.plot_surface(X, Y, Z, alpha=0.3, cmap='viridis')
    
    # Overlay the spirals on the torus surface
    theta_spiral = np.linspace(0, 4*np.pi, 500)
    for phase in [0, np.pi/2, np.pi, 3*np.pi/2]:
        x_tor = (R + r_minor * np.cos(theta_spiral)) * np.cos(theta_spiral + phase)
        y_tor = (R + r_minor * np.cos(theta_spiral)) * np.sin(theta_spiral + phase)
        z_tor = r_minor * np.sin(theta_spiral)
        ax2.plot(x_tor, y_tor, z_tor, linewidth=2)
    
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title(f'Toroidal Field (R/r = φ²)', fontsize=14, fontweight='bold')
    ax2.text2D(0.05, 0.95, f'φ = {PHI:.6f}', transform=ax2.transAxes, fontsize=10,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig

def analyze_connection_properties():
    """Analyze the mathematical properties of the connection"""
    print("=" * 60)
    print("GOLDEN SPIRAL MIRRORING: Mathematical Analysis")
    print("=" * 60)
    
    print(f"\n1. Golden Ratio φ = {PHI:.10f}")
    print(f"   φ² = {PHI**2:.10f}")
    print(f"   1/φ = {1/PHI:.10f}")
    print(f"   φ - 1 = 1/φ: {abs(PHI - 1 - 1/PHI) < 1e-10}")
    
    print("\n2. Spiral Equation:")
    print("   r(θ) = a × φ^(2θ/π)")
    print("   This is a logarithmic spiral with growth factor φ")
    
    print("\n3. Self-Similarity:")
    print(f"   Growth per 90° turn: φ^(2×π/2÷π) = φ = {PHI:.6f}")
    print(f"   Growth per 180° turn: φ² = {PHI**2:.6f}")
    print(f"   Growth per 360° turn: φ⁴ = {PHI**4:.6f}")
    
    print("\n4. Tangent Angle α(θ):")
    print("   tan(α) = r/(dr/dθ) = constant = π/(2×ln(φ))")
    angle_deg = np.degrees(np.arctan(np.pi / (2 * np.log(PHI))))
    print(f"   α ≈ {angle_deg:.2f}°")
    print("   This constant angle ensures smooth connection!")
    
    print("\n5. Connection at Center:")
    print("   As θ → -∞, r → 0 (spirals inward to singularity)")
    print("   Four spirals meet at (0,0) with continuous tangency")
    
    print("\n6. Applications:")
    print("   • Nature: Nautilus shells, hurricanes, galaxies")
    print("   • Art: Logo design, sacred geometry")
    print("   • Physics: Vortex dynamics, electromagnetic fields")
    print("   • Biology: DNA helices, seed patterns")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Print mathematical analysis
    analyze_connection_properties()
    
    # Create visualizations
    print("\nGenerating 2D visualization...")
    fig_2d = create_2d_visualization()
    fig_2d.savefig('golden_mirror_2d.png', dpi=300, bbox_inches='tight')
    print("Saved: golden_mirror_2d.png")
    
    print("Generating 3D visualization...")
    fig_3d = create_3d_visualization()
    fig_3d.savefig('golden_mirror_3d.png', dpi=300, bbox_inches='tight')
    print("Saved: golden_mirror_3d.png")
    
    print("\n✨ Visualizations complete! Check the PNG files.")
    plt.close('all')
