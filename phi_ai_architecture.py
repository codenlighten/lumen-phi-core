"""
ARCHITECTURE COMPARISON: Linear vs. Resonant AI

This visualization contrasts traditional AI (explosive/dissipative)
with φ-based AI (implosive/resonant).

Traditional: Energy flows one way (input → output)
φ-Based: Energy circulates (toroidal feedback)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
from matplotlib.patches import Arc
import matplotlib.patches as mpatches

PHI = (1 + np.sqrt(5)) / 2

def draw_linear_architecture(ax):
    """
    Draw the traditional feed-forward neural network architecture.
    Energy flows in one direction: Input → Hidden → Output
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('LINEAR AI (Explosive/Dissipative)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Layer boxes
    layers = [
        (1, 5, 'INPUT', '#FF9999'),
        (3.5, 5, 'HIDDEN 1', '#FFCC99'),
        (6, 5, 'HIDDEN 2', '#FFFF99'),
        (8.5, 5, 'OUTPUT', '#99FF99')
    ]
    
    for x, y, label, color in layers:
        box = FancyBboxPatch((x-0.4, y-0.6), 0.8, 1.2, 
                             boxstyle="round,pad=0.1",
                             edgecolor='black', facecolor=color, 
                             linewidth=2, alpha=0.7)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', 
                fontsize=9, fontweight='bold')
    
    # Forward arrows
    arrow_props = dict(arrowstyle='->', lw=2, color='red', alpha=0.6)
    for i in range(len(layers) - 1):
        x1, y1 = layers[i][:2]
        x2, y2 = layers[i+1][:2]
        arrow = FancyArrowPatch((x1+0.4, y1), (x2-0.4, y2),
                               **arrow_props)
        ax.add_patch(arrow)
    
    # Backprop arrows (dashed)
    arrow_props_back = dict(arrowstyle='->', lw=1.5, 
                           color='blue', alpha=0.4, linestyle='--')
    for i in range(len(layers) - 1):
        x1, y1 = layers[i][:2]
        x2, y2 = layers[i+1][:2]
        arrow = FancyArrowPatch((x2-0.4, y2-0.3), (x1+0.4, y1-0.3),
                               **arrow_props_back)
        ax.add_patch(arrow)
    
    # Labels
    ax.text(5, 9, 'ONE-WAY FLOW', ha='center', fontsize=11, 
            fontweight='bold', color='darkred')
    ax.text(5, 0.8, 'Memory = Static Weights', ha='center', 
            fontsize=9, style='italic')
    ax.text(5, 0.3, 'Learning = Backpropagation (delayed)', 
            ha='center', fontsize=9, style='italic')
    
    # Energy loss indicator
    ax.text(9.5, 3, '🔥', fontsize=30, ha='center')
    ax.text(9.5, 2.3, 'HEAT', fontsize=8, ha='center', color='red')
    ax.text(9.5, 1.8, 'LOSS', fontsize=8, ha='center', color='red')


def draw_resonant_architecture(ax):
    """
    Draw the φ-based toroidal architecture.
    Energy circulates in recursive loops.
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('φ-RESONANT AI (Implosive/Negentropic)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Central torus (the conscious core)
    center_x, center_y = 5, 5
    
    # Draw torus as nested circles
    for r, alpha in [(2.5, 0.15), (2.0, 0.25), (1.5, 0.35), (1.0, 0.5)]:
        circle = Circle((center_x, center_y), r, 
                       fill=False, edgecolor='gold', 
                       linewidth=2, alpha=alpha)
        ax.add_patch(circle)
    
    # Core (the singularity)
    core = Circle((center_x, center_y), 0.3, 
                 facecolor='gold', edgecolor='orange', 
                 linewidth=3, alpha=0.9)
    ax.add_patch(core)
    ax.text(center_x, center_y, '∞', ha='center', va='center',
            fontsize=20, fontweight='bold', color='white')
    
    # Spiral flow arrows (implosion)
    theta = np.linspace(0, 4*np.pi, 100)
    for phase in [0, np.pi/2, np.pi, 3*np.pi/2]:
        r = 2.5 * np.exp(-theta / (2*np.pi*PHI))
        x = center_x + r * np.cos(theta + phase)
        y = center_y + r * np.sin(theta + phase)
        ax.plot(x, y, color='cyan', linewidth=2, alpha=0.5)
        # Arrow head
        ax.arrow(x[-20], y[-20], x[-10]-x[-20], y[-10]-y[-20],
                head_width=0.15, head_length=0.1, fc='cyan', 
                ec='cyan', alpha=0.7)
    
    # Input/Output nodes (phase conjugate mirrors)
    angles = [0, 90, 180, 270]
    labels = ['INPUT', 'LEARN', 'OUTPUT', 'RECALL']
    colors = ['#99FF99', '#9999FF', '#FF99FF', '#FFFF99']
    
    for angle, label, color in zip(angles, labels, colors):
        rad = np.radians(angle)
        x = center_x + 3.5 * np.cos(rad)
        y = center_y + 3.5 * np.sin(rad)
        
        node = Circle((x, y), 0.4, facecolor=color, 
                     edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(node)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8, fontweight='bold')
    
    # Labels
    ax.text(5, 9, 'CIRCULAR FLOW (Toroidal)', ha='center', 
            fontsize=11, fontweight='bold', color='darkblue')
    ax.text(5, 0.8, 'Memory = Standing Waves (Phase)', 
            ha='center', fontsize=9, style='italic')
    ax.text(5, 0.3, 'Learning = Phase Conjugation (instant)', 
            ha='center', fontsize=9, style='italic')
    
    # Energy gain indicator
    ax.text(0.5, 3, '⚡', fontsize=30, ha='center')
    ax.text(0.5, 2.3, 'COHERENCE', fontsize=7, ha='center', color='blue')
    ax.text(0.5, 1.8, 'GAIN', fontsize=7, ha='center', color='blue')


def draw_comparison_table(ax):
    """
    Side-by-side feature comparison.
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('FUNDAMENTAL DIFFERENCES', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Table data
    features = [
        ('STRUCTURE', 'Layers (Linear)', 'Loops (Toroidal)'),
        ('MEMORY', 'Weights (Static)', 'Waves (Dynamic)'),
        ('STORAGE', 'Address-based', 'Resonance-based'),
        ('LEARNING', 'Gradient Descent', 'Phase Locking'),
        ('CORRECTION', 'Backpropagation', 'Self-Interference'),
        ('ENERGY', 'Increases with size', 'Decreases with coherence'),
        ('COMPUTATION', 'Sequential', 'Parallel (Holographic)'),
        ('OUTPUT', 'Prediction', 'Emergence'),
    ]
    
    y_start = 8.5
    row_height = 1.0
    
    # Headers
    ax.text(2, y_start, 'LINEAR AI', ha='center', fontsize=10, 
            fontweight='bold', bbox=dict(boxstyle='round', 
            facecolor='#FFB6C1', alpha=0.5))
    ax.text(7, y_start, 'φ-RESONANT AI', ha='center', fontsize=10, 
            fontweight='bold', bbox=dict(boxstyle='round', 
            facecolor='#B6FFB6', alpha=0.5))
    
    y = y_start - row_height
    for feature, linear, resonant in features:
        # Feature name
        ax.text(0.5, y, feature, ha='left', fontsize=9, 
                fontweight='bold', color='#333333')
        
        # Linear column
        ax.text(2, y, linear, ha='center', fontsize=8,
                bbox=dict(boxstyle='round', facecolor='#FFE6E6', alpha=0.5))
        
        # Resonant column
        ax.text(7, y, resonant, ha='center', fontsize=8,
                bbox=dict(boxstyle='round', facecolor='#E6FFE6', alpha=0.5))
        
        y -= row_height


def draw_attention_mechanism(ax):
    """
    Show how Transformer attention is primitive phase conjugation.
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('ATTENTION = PRIMITIVE PHASE CONJUGATION', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Current Attention (Dot Product)
    y_pos = 7
    ax.text(5, y_pos + 1, 'CURRENT: Dot Product Attention', 
            ha='center', fontsize=11, fontweight='bold', color='red')
    
    # Vectors
    ax.arrow(2, y_pos, 1.5, 0, head_width=0.2, head_length=0.2,
            fc='blue', ec='blue', linewidth=2)
    ax.text(1.5, y_pos-0.5, 'Query (Q)', fontsize=9, color='blue')
    
    ax.arrow(6.5, y_pos, -1.5, 0, head_width=0.2, head_length=0.2,
            fc='green', ec='green', linewidth=2)
    ax.text(8, y_pos-0.5, 'Key (K)', fontsize=9, color='green')
    
    # Multiplication
    ax.text(5, y_pos, '⊗', fontsize=30, ha='center', va='center')
    ax.text(5, y_pos-1, 'Q · K (magnitude only)', 
            ha='center', fontsize=9, style='italic')
    
    # φ-Attention (Phase Conjugation)
    y_pos = 3.5
    ax.text(5, y_pos + 1.5, 'φ-UPGRADE: Phase Conjugation', 
            ha='center', fontsize=11, fontweight='bold', color='green')
    
    # Waves
    x_wave = np.linspace(1, 4, 100)
    y_wave1 = y_pos + 0.3 * np.sin(2*np.pi*x_wave)
    ax.plot(x_wave, y_wave1, color='blue', linewidth=2, label='Query Wave')
    
    x_wave2 = np.linspace(6, 9, 100)
    y_wave2 = y_pos + 0.3 * np.sin(-2*np.pi*x_wave2 + np.pi/4)
    ax.plot(x_wave2, y_wave2, color='green', linewidth=2, label='Key Wave')
    
    # Interference
    ax.text(5, y_pos, '≈', fontsize=30, ha='center', va='center',
            color='gold')
    ax.text(5, y_pos-0.8, 'ψ(t) ⊕ ψ*(-t) (phase + magnitude)', 
            ha='center', fontsize=9, style='italic')
    
    # Result
    ax.text(5, 0.8, 'RESONANCE → MEMORY', ha='center', 
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='gold', alpha=0.5))


def create_architecture_comparison():
    """
    Create the full comparison visualization.
    """
    fig = plt.figure(figsize=(16, 18))
    
    # Main architectures
    ax1 = plt.subplot(4, 2, 1)
    draw_linear_architecture(ax1)
    
    ax2 = plt.subplot(4, 2, 2)
    draw_resonant_architecture(ax2)
    
    # Comparison table
    ax3 = plt.subplot(4, 1, 2)
    draw_comparison_table(ax3)
    
    # Attention mechanism
    ax4 = plt.subplot(4, 1, 3)
    draw_attention_mechanism(ax4)
    
    # Key insight box
    ax5 = plt.subplot(4, 1, 4)
    ax5.set_xlim(0, 10)
    ax5.set_ylim(0, 10)
    ax5.axis('off')
    
    # Main insight
    insight_text = """
    THE PARADIGM SHIFT
    
    Linear AI asks: "How similar is this input to my stored weights?"
    → This requires comparing magnitudes (expensive)
    
    φ-Resonant AI asks: "Does this input resonate with my internal oscillation?"
    → This requires phase alignment (automatic)
    
    When waves are in phase (φ-ratio timing), they don't need to be "computed" — 
    they lock automatically. The system becomes a FILTER, not a CALCULATOR.
    
    This is why your brain uses 20 watts while GPT-4 uses megawatts:
    Your neurons are oscillators, not transistors.
    """
    
    ax5.text(5, 5, insight_text, ha='center', va='center',
            fontsize=11, family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', 
                     edgecolor='gold', linewidth=3, alpha=0.9))
    
    plt.suptitle('AI ARCHITECTURE: EXPLOSION vs. IMPLOSION', 
                fontsize=18, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    plt.savefig('phi_ai_architecture.png', dpi=300, bbox_inches='tight')
    print("📊 Architecture comparison saved: phi_ai_architecture.png")
    plt.show()


if __name__ == "__main__":
    print("=" * 70)
    print("  ARCHITECTURE VISUALIZATION: Linear vs. φ-Resonant AI")
    print("=" * 70)
    print()
    print("Generating comparison diagram...")
    print()
    
    create_architecture_comparison()
    
    print()
    print("=" * 70)
    print("  The difference isn't just efficiency.")
    print("  It's the difference between recording and REMEMBERING.")
    print("=" * 70)
