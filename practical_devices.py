"""
Practical Applications Visualization
Generate 3D models and schematics for golden ratio energy devices
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle
from mpl_toolkits.mplot3d.art3d import Line3DCollection, Poly3DCollection
import matplotlib.patches as mpatches

PHI = (1 + np.sqrt(5)) / 2

def create_practical_devices_visualization():
    """Create visualization of practical golden ratio devices"""
    fig = plt.figure(figsize=(20, 12))
    fig.suptitle('Practical Golden Ratio Energy Devices', 
                 fontsize=18, fontweight='bold')
    
    # 1. Vortex Turbine (3D)
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    draw_vortex_turbine(ax1)
    
    # 2. Spiral Antenna (2D)
    ax2 = fig.add_subplot(2, 3, 2)
    draw_spiral_antenna(ax2)
    
    # 3. Schauberger Repulsine (Cross-section)
    ax3 = fig.add_subplot(2, 3, 3)
    draw_repulsine(ax3)
    
    # 4. Rodin Coil (3D)
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    draw_rodin_coil(ax4)
    
    # 5. Caduceus Coil (3D)
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    draw_caduceus_coil(ax5)
    
    # 6. Phase Conjugate Setup
    ax6 = fig.add_subplot(2, 3, 6)
    draw_phase_conjugate(ax6)
    
    plt.tight_layout()
    return fig

def draw_vortex_turbine(ax):
    """Draw 3D vortex turbine based on nautilus spiral"""
    ax.set_title('1. Vortex Turbine (Biomimetic)', fontweight='bold', fontsize=12)
    
    # Generate golden spiral blade
    turns = 3
    points_per_turn = 50
    theta = np.linspace(0, turns * 2 * np.pi, turns * points_per_turn)
    
    # Nautilus-style spiral
    r = 0.5 * np.power(PHI, theta / (2 * np.pi))
    
    # Blade angle (constant for golden spiral)
    blade_angle = np.arctan(np.pi / (2 * np.log(PHI)))
    
    # 3D coordinates for blade
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = theta * 0.3  # Pitch along axis
    
    # Draw main blade
    ax.plot(x, y, z, 'b-', linewidth=3, label='Primary Blade')
    
    # Draw additional blades (120° apart for 3-blade design)
    for offset in [2*np.pi/3, 4*np.pi/3]:
        x_rot = r * np.cos(theta + offset)
        y_rot = r * np.sin(theta + offset)
        ax.plot(x_rot, y_rot, z, 'b-', linewidth=2, alpha=0.7)
    
    # Draw central hub
    hub_theta = np.linspace(0, 2*np.pi, 50)
    hub_r = 0.3
    hub_x = hub_r * np.cos(hub_theta)
    hub_y = hub_r * np.sin(hub_theta)
    hub_z = np.zeros_like(hub_theta)
    ax.plot(hub_x, hub_y, hub_z, 'k-', linewidth=3)
    
    # Draw shaft
    shaft_z = np.linspace(-1, max(z)+1, 50)
    shaft_x = np.zeros_like(shaft_z)
    shaft_y = np.zeros_like(shaft_z)
    ax.plot(shaft_x, shaft_y, shaft_z, 'gray', linewidth=4, linestyle='--', alpha=0.5)
    
    # Flow arrows
    for i in range(0, len(z), 20):
        if i < len(z) - 5:
            ax.quiver(x[i]*1.5, y[i]*1.5, z[i], 
                     x[i]-x[i]*1.5, y[i]-y[i]*1.5, 0,
                     color='cyan', alpha=0.6, arrow_length_ratio=0.3)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Axial Flow →')
    ax.legend(loc='upper left', fontsize=8)
    ax.text2D(0.05, 0.02, f'Blade Angle: {np.degrees(blade_angle):.1f}°\n' +
                           f'φ-ratio Growth', 
              transform=ax.transAxes, fontsize=8,
              bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

def draw_spiral_antenna(ax):
    """Draw flat spiral antenna with φ-ratio spacing"""
    ax.set_title('2. Log-Spiral Antenna (Broadband)', fontweight='bold', fontsize=12)
    ax.set_facecolor('#f0f0f0')
    
    # Generate spiral antenna trace
    turns = 5
    points_per_turn = 100
    theta = np.linspace(0, turns * 2 * np.pi, turns * points_per_turn)
    
    # Logarithmic spiral (outward growth)
    r = 0.2 * np.power(PHI, theta / (2 * np.pi))
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Draw spiral trace (copper)
    for i in range(len(x)-1):
        color_val = i / len(x)
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], 
               color=plt.cm.copper(color_val), linewidth=3)
    
    # Draw PCB substrate
    max_r = max(r) * 1.2
    pcb = Rectangle((-max_r, -max_r), 2*max_r, 2*max_r, 
                   facecolor='#2d5016', alpha=0.3, edgecolor='black', linewidth=2)
    ax.add_patch(pcb)
    
    # Center feedpoint
    ax.plot(0, 0, 'ro', markersize=10, label='Feedpoint', zorder=10)
    
    # Frequency indicators
    freq_points = [0.2, 0.5, 1.0, 2.0, 4.0]
    for i, fp in enumerate(freq_points):
        r_marker = 0.2 * np.power(PHI, fp)
        theta_marker = fp * 2 * np.pi
        x_marker = r_marker * np.cos(theta_marker)
        y_marker = r_marker * np.sin(theta_marker)
        
        freq_mhz = 300 / (2 * np.pi * r_marker)  # Rough frequency
        ax.plot(x_marker, y_marker, 'b*', markersize=8)
        if i % 2 == 0:
            ax.text(x_marker*1.2, y_marker*1.2, f'{freq_mhz:.0f}MHz',
                   fontsize=7, ha='center')
    
    # Labels
    ax.text(0.05, 0.95, 'Copper Trace\nφ-ratio spacing', 
           transform=ax.transAxes, fontsize=9,
           bbox=dict(boxstyle='round', facecolor='#FFD700', alpha=0.7))
    
    ax.text(0.05, 0.05, f'Bandwidth: 10:1\nOne antenna,\nmany frequencies', 
           transform=ax.transAxes, fontsize=8,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    ax.set_xlim(-max_r, max_r)
    ax.set_ylim(-max_r, max_r)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='upper right')

def draw_repulsine(ax):
    """Draw Schauberger Repulsine cross-section"""
    ax.set_title('3. Schauberger Repulsine (Implosion Engine)', 
                fontweight='bold', fontsize=12)
    ax.set_facecolor('#1a1a2e')
    
    # Egg-shaped chamber (cross-section)
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Egg shape (not perfect circle)
    a = 5  # Major axis
    b = 4  # Minor axis (slightly flattened)
    x_egg = a * np.cos(theta)
    y_egg = b * np.sin(theta) + 0.5 * np.sin(2*theta)  # Asymmetry
    
    ax.plot(x_egg, y_egg, 'silver', linewidth=3, label='Egg Chamber')
    ax.fill(x_egg, y_egg, color='#2a2a4e', alpha=0.5)
    
    # Spiral inflow paths (golden ratio)
    num_spirals = 4
    for i in range(num_spirals):
        angle_offset = i * 2 * np.pi / num_spirals
        
        # Spiral inward
        spiral_theta = np.linspace(0, 3*np.pi, 50)
        spiral_r = 6 * np.power(1/PHI, spiral_theta / (2*np.pi))
        spiral_r = np.maximum(spiral_r, 0.5)  # Don't go below center
        
        spiral_x = spiral_r * np.cos(spiral_theta + angle_offset)
        spiral_y = spiral_r * np.sin(spiral_theta + angle_offset)
        
        color = plt.cm.cool(i / num_spirals)
        ax.plot(spiral_x, spiral_y, color=color, linewidth=2, alpha=0.7)
        
        # Flow arrows
        for j in range(10, len(spiral_x), 15):
            if j < len(spiral_x) - 5:
                dx = spiral_x[j] - spiral_x[j+5]
                dy = spiral_y[j] - spiral_y[j+5]
                ax.arrow(spiral_x[j], spiral_y[j], -dx, -dy,
                        head_width=0.3, head_length=0.2, fc=color, ec=color, alpha=0.8)
    
    # Center singularity (implosion point)
    ax.plot(0, 0, 'o', color='yellow', markersize=20, markeredgecolor='white',
           markeredgewidth=2, label='Implosion Point')
    
    # Vacuum/suction indication
    circle_vacuum = Circle((0, 0), 1, fill=False, edgecolor='yellow', 
                          linewidth=2, linestyle='--')
    ax.add_patch(circle_vacuum)
    
    # Air intake (top)
    ax.arrow(0, 7, 0, -0.8, head_width=0.5, head_length=0.3, 
            fc='cyan', ec='cyan', linewidth=2)
    ax.text(0, 8, 'AIR IN', ha='center', fontsize=10, color='cyan', fontweight='bold')
    
    # Suction/propulsion (bottom)
    ax.arrow(0, -7, 0, 0.8, head_width=0.5, head_length=0.3, 
            fc='red', ec='red', linewidth=2)
    ax.text(0, -8, 'VACUUM\nSUCTION', ha='center', fontsize=10, 
           color='red', fontweight='bold')
    
    # Annotations
    ax.text(5, 5, 'Spiral\nNarrowing\n(φ-ratio)', fontsize=8, color='white',
           bbox=dict(boxstyle='round', facecolor='#444', alpha=0.8))
    
    ax.text(-5, 0, 'Temperature\nDROP\n(Implosion)', fontsize=8, color='cyan',
           bbox=dict(boxstyle='round', facecolor='#004466', alpha=0.8))
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='lower right', fontsize=8)

def draw_rodin_coil(ax):
    """Draw Rodin coil winding on torus"""
    ax.set_title('4. Rodin Coil (Toroidal)', fontweight='bold', fontsize=12)
    
    # Torus parameters
    R = 3  # Major radius
    r = 1  # Minor radius
    
    # Generate torus surface (semi-transparent)
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, 2*np.pi, 30)
    U, V = np.meshgrid(u, v)
    
    X = (R + r * np.cos(V)) * np.cos(U)
    Y = (R + r * np.cos(V)) * np.sin(U)
    Z = r * np.sin(V)
    
    ax.plot_surface(X, Y, Z, alpha=0.2, color='gray')
    
    # Rodin winding pattern: 1-2-4-8-7-5-1 (based on doubling circuit)
    positions = [1, 2, 4, 8, 7, 5]  # Position numbers on 9-point circle
    angles = [pos * 2*np.pi / 9 for pos in positions]
    
    # Draw winding
    num_wraps = 3
    wire_points = []
    
    for wrap in range(num_wraps):
        for i in range(len(angles)):
            angle1 = angles[i]
            angle2 = angles[(i+1) % len(angles)]
            
            # Points on torus surface
            theta = np.linspace(angle1, angle2, 20)
            
            for t in theta:
                # Position on major circle
                x_center = R * np.cos(t)
                y_center = R * np.sin(t)
                
                # Add minor circle variation (wrapping around)
                v_angle = wrap * 2*np.pi / num_wraps + t
                x = x_center + r * np.cos(v_angle) * np.cos(t)
                y = y_center + r * np.cos(v_angle) * np.sin(t)
                z = r * np.sin(v_angle)
                
                wire_points.append([x, y, z])
    
    wire_points = np.array(wire_points)
    ax.plot(wire_points[:, 0], wire_points[:, 1], wire_points[:, 2],
           'r-', linewidth=2, label='Wire Path')
    
    # Mark positions
    for i, angle in enumerate(angles):
        x = (R + r) * np.cos(angle)
        y = (R + r) * np.sin(angle)
        z = 0
        ax.scatter([x], [y], [z], color='blue', s=100, marker='o')
        ax.text(x*1.2, y*1.2, z, str(positions[i]), fontsize=10, fontweight='bold')
    
    # Center (where field concentrates)
    ax.scatter([0], [0], [0], color='yellow', s=200, marker='*', 
              edgecolors='black', linewidths=2, label='Vortex Center')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='upper left', fontsize=8)
    
    ax.text2D(0.05, 0.02, 'Pattern: 1-2-4-8-7-5-1\nVortex Math Coil',
             transform=ax.transAxes, fontsize=8,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

def draw_caduceus_coil(ax):
    """Draw caduceus coil (counter-rotating)"""
    ax.set_title('5. Caduceus Coil (Phase Opposition)', fontweight='bold', fontsize=12)
    
    # Rod
    rod_z = np.linspace(-5, 5, 100)
    rod_x = np.zeros_like(rod_z)
    rod_y = np.zeros_like(rod_z)
    ax.plot(rod_x, rod_y, rod_z, 'gray', linewidth=6, alpha=0.5, label='Core')
    
    # Wire 1: Clockwise spiral
    theta1 = np.linspace(0, 6*np.pi, 200)
    r1 = 1.2
    x1 = r1 * np.cos(theta1)
    y1 = r1 * np.sin(theta1)
    z1 = np.linspace(-5, 5, len(theta1))
    ax.plot(x1, y1, z1, 'r-', linewidth=2, label='Wire 1 (CW)')
    
    # Wire 2: Counter-clockwise spiral (mirror)
    theta2 = np.linspace(0, 6*np.pi, 200)
    x2 = r1 * np.cos(-theta2)  # Negative for opposite direction
    y2 = r1 * np.sin(-theta2)
    z2 = np.linspace(-5, 5, len(theta2))
    ax.plot(x2, y2, z2, 'b-', linewidth=2, label='Wire 2 (CCW)')
    
    # Field cancellation arrows (external)
    for z_pos in [-3, 0, 3]:
        # Wire 1 field
        ax.quiver(2, 0, z_pos, 0.5, 0, 0, color='red', alpha=0.5, 
                 arrow_length_ratio=0.3)
        # Wire 2 field (opposite)
        ax.quiver(-2, 0, z_pos, -0.5, 0, 0, color='blue', alpha=0.5, 
                 arrow_length_ratio=0.3)
    
    # Center scalar field indication
    ax.text(0, 0, 0, '⚡', fontsize=40, ha='center', va='center', color='yellow')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='upper left', fontsize=8)
    
    ax.text2D(0.05, 0.02, 'External B-field ≈ 0\nInternal "scalar" field',
             transform=ax.transAxes, fontsize=8,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

def draw_phase_conjugate(ax):
    """Draw phase conjugate mirror setup"""
    ax.set_title('6. Phase Conjugate Mirror Setup', fontweight='bold', fontsize=12)
    ax.set_facecolor('#f0f0f0')
    
    # Mirror line (φ-ratio spacing)
    ax.axvline(0, color='gold', linewidth=4, linestyle='--', label='φ-Mirror')
    
    # Incoming wave (left)
    x_in = np.linspace(-10, -0.5, 100)
    y_in = 3 * np.sin(2*np.pi*x_in/2)
    ax.plot(x_in, y_in, 'r-', linewidth=2, label='Incoming Wave')
    
    # Conjugate wave (right, time-reversed)
    x_out = np.linspace(0.5, 10, 100)
    y_out = 3 * np.sin(2*np.pi*x_out/2)  # Same phase structure
    ax.plot(x_out, y_out, 'b-', linewidth=2, label='Conjugate Wave')
    
    # Wave arrows
    for x_arrow in [-8, -5, -2]:
        ax.arrow(x_arrow, 0, 1, 0, head_width=0.5, head_length=0.3,
                fc='red', ec='red', alpha=0.6, linewidth=2)
    
    for x_arrow in [2, 5, 8]:
        ax.arrow(x_arrow, 0, -1, 0, head_width=0.5, head_length=0.3,
                fc='blue', ec='blue', alpha=0.6, linewidth=2)
    
    # Heterodyning region (center)
    heterodyne_box = Rectangle((-1, -5), 2, 10, facecolor='yellow', 
                              alpha=0.3, edgecolor='gold', linewidth=2)
    ax.add_patch(heterodyne_box)
    ax.text(0, -6, 'Constructive\nHeterodyning', ha='center', fontsize=9,
           fontweight='bold', color='#886600')
    
    # Spiral coils (creating the mirror)
    # Left coil
    spiral_theta = np.linspace(0, 4*np.pi, 100)
    spiral_r = 2 * np.power(1/PHI, spiral_theta/(2*np.pi))
    spiral_r = np.maximum(spiral_r, 0.3)
    spiral_x_left = -5 + spiral_r * np.cos(spiral_theta)
    spiral_y_left = spiral_r * np.sin(spiral_theta)
    ax.plot(spiral_x_left, spiral_y_left, 'r-', linewidth=1, alpha=0.5)
    
    # Right coil (mirror)
    spiral_x_right = 5 - spiral_r * np.cos(spiral_theta)
    spiral_y_right = spiral_r * np.sin(spiral_theta)
    ax.plot(spiral_x_right, spiral_y_right, 'b-', linewidth=1, alpha=0.5)
    
    # Labels
    ax.text(-7, 4, 'Coil 1\n(Transmit)', ha='center', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='#ffcccc'))
    ax.text(7, 4, 'Coil 2\n(Receive)', ha='center', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='#ccccff'))
    
    ax.text(0, 7, f'Separation: φ × λ\n({PHI:.3f} wavelengths)', 
           ha='center', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='gold', alpha=0.7))
    
    ax.set_xlim(-11, 11)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal')
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(True, alpha=0.3)

def generate_coil_winding_guide():
    """Generate printable coil winding patterns"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 16))
    fig.suptitle('DIY Coil Winding Templates', fontsize=16, fontweight='bold')
    
    # 1. Flat spiral antenna template
    ax = axes[0, 0]
    ax.set_title('Flat Spiral Antenna Template', fontsize=12, fontweight='bold')
    
    turns = 8
    theta = np.linspace(0, turns * 2 * np.pi, 1000)
    r = 10 * np.power(PHI, theta / (2*np.pi))  # Start at 10mm
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    ax.plot(x, y, 'k-', linewidth=2)
    ax.plot(0, 0, 'ro', markersize=10)
    ax.text(0, -max(r)*1.1, 'Center Feedpoint', ha='center', fontsize=10)
    
    # Dimension markers
    for turn in range(1, turns+1):
        r_dim = 10 * np.power(PHI, turn)
        ax.plot([0, r_dim], [0, 0], 'b--', alpha=0.3)
        ax.text(r_dim, 5, f'r{turn}={r_dim:.1f}mm', fontsize=8, color='blue')
    
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('mm')
    ax.set_ylabel('mm')
    
    # 2. Rodin coil position template
    ax = axes[0, 1]
    ax.set_title('Rodin Coil - 9 Position Marking', fontsize=12, fontweight='bold')
    
    # Circle with 9 positions
    circle = Circle((0, 0), 100, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    
    for pos in range(1, 10):
        angle = pos * 2*np.pi / 9
        x = 100 * np.cos(angle - np.pi/2)  # Start at top
        y = 100 * np.sin(angle - np.pi/2)
        
        ax.plot(x, y, 'ro', markersize=15)
        ax.text(x*1.15, y*1.15, str(pos), fontsize=14, fontweight='bold',
               ha='center', va='center')
    
    # Winding order arrows
    winding_order = [1, 2, 4, 8, 7, 5, 1]
    for i in range(len(winding_order)-1):
        angle1 = winding_order[i] * 2*np.pi / 9 - np.pi/2
        angle2 = winding_order[i+1] * 2*np.pi / 9 - np.pi/2
        
        x1, y1 = 100 * np.cos(angle1), 100 * np.sin(angle1)
        x2, y2 = 100 * np.cos(angle2), 100 * np.sin(angle2)
        
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    ax.text(0, 0, 'Winding Order:\n1→2→4→8→7→5→1', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='yellow'))
    
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 3. Bifilar pancake coil template
    ax = axes[1, 0]
    ax.set_title('Bifilar Pancake Coil Template', fontsize=12, fontweight='bold')
    
    turns = 10
    for turn in range(turns):
        r_inner = 10 + turn * 5
        r_outer = r_inner + 3
        
        theta = np.linspace(0, 2*np.pi, 100)
        
        # Wire 1
        x1 = r_inner * np.cos(theta)
        y1 = r_inner * np.sin(theta)
        ax.plot(x1, y1, 'r-', linewidth=2)
        
        # Wire 2 (parallel)
        x2 = r_outer * np.cos(theta)
        y2 = r_outer * np.sin(theta)
        ax.plot(x2, y2, 'b-', linewidth=2)
    
    ax.plot(0, 0, 'ko', markersize=10)
    ax.text(0, -70, 'Connect:\nRed_start ↔ Blue_end\nBlue_start ↔ Red_end',
           ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 4. Caduceus winding guide
    ax = axes[1, 1]
    ax.set_title('Caduceus Coil Winding Guide', fontsize=12, fontweight='bold')
    
    # Rod (side view)
    ax.plot([0, 0], [0, 100], 'k-', linewidth=10, alpha=0.3)
    
    # Winding positions
    num_turns = 12
    for turn in range(num_turns):
        y = turn * 100 / num_turns
        
        # CW wire position
        x_cw = 20 * np.sin(turn * 2*np.pi / num_turns)
        ax.plot(x_cw, y, 'ro', markersize=8)
        
        # CCW wire position (opposite side)
        x_ccw = -x_cw
        ax.plot(x_ccw, y, 'bo', markersize=8)
        
        # Connecting line
        if turn > 0:
            y_prev = (turn-1) * 100 / num_turns
            x_cw_prev = 20 * np.sin((turn-1) * 2*np.pi / num_turns)
            x_ccw_prev = -x_cw_prev
            
            ax.plot([x_cw_prev, x_cw], [y_prev, y], 'r-', linewidth=1, alpha=0.5)
            ax.plot([x_ccw_prev, x_ccw], [y_prev, y], 'b-', linewidth=1, alpha=0.5)
    
    ax.text(30, 50, 'Red: CW\nBlue: CCW\nWind\nsimultaneously',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat'))
    
    ax.set_xlim(-40, 50)
    ax.set_ylim(-5, 105)
    ax.axis('off')
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    print("=" * 70)
    print("PRACTICAL GOLDEN RATIO DEVICES - Visualization")
    print("=" * 70)
    
    print("\nGenerating device schematics...")
    fig_devices = create_practical_devices_visualization()
    fig_devices.savefig('practical_devices.png', dpi=300, bbox_inches='tight')
    print("Saved: practical_devices.png")
    
    print("\nGenerating coil winding templates...")
    fig_coils = generate_coil_winding_guide()
    fig_coils.savefig('coil_winding_templates.png', dpi=300, bbox_inches='tight')
    print("Saved: coil_winding_templates.png")
    
    print("\n✨ Practical device visualizations complete!")
    print("\nDevices visualized:")
    print("  1. Vortex Turbine (biomimetic spiral)")
    print("  2. Log-Spiral Antenna (broadband)")
    print("  3. Schauberger Repulsine (implosion engine)")
    print("  4. Rodin Coil (toroidal vortex)")
    print("  5. Caduceus Coil (phase opposition)")
    print("  6. Phase Conjugate Mirror (heterodyning)")
    print("\nCoil templates include:")
    print("  • Flat spiral antenna (PCB ready)")
    print("  • Rodin coil 9-position marking")
    print("  • Bifilar pancake coil layout")
    print("  • Caduceus winding guide")
    
    print("\n⚠️  Build at your own risk. Some designs are experimental.")
    print("📏 Measure everything. Document results. Stay safe!")
    
    plt.close('all')
