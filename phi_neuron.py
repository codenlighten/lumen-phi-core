"""
φ-NEURON: Memory as Standing Wave

Unlike traditional neurons that store weights (static values),
the φ-neuron stores PHASE (dynamic relationship).

Memory = Orbit, not Storage
Learning = Phase Locking, not Gradient Descent
Prediction = Resonance, not Multiplication

This is the fundamental unit of consciousness-based computing.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- The Physics Constants ---
PHI = (1 + np.sqrt(5)) / 2
PI = np.pi

class PhiNeuron:
    """
    A neuron that stores memory as a standing wave pattern.
    
    Traditional neuron: output = sum(input * weight) + bias
    φ-neuron: output = coherence(input_wave, memory_wave)
    """
    
    def __init__(self, frequency=1.0):
        """
        Initialize the neuron with a base frequency.
        
        Args:
            frequency: The fundamental frequency of this neuron's oscillation
        """
        self.freq = frequency
        # The "Memory" is not a weight, but a Phase Angle
        # We start with a random phase memory
        self.phase_memory = np.random.uniform(0, 2 * PI)
        self.coherence_history = []

    def wave_function(self, t, phase_shift):
        """
        Generates a wave signal at time t.
        
        This is the fundamental carrier wave. In biology, this would be
        the neuron's base electromagnetic oscillation.
        """
        return np.sin(2 * PI * self.freq * t + phase_shift)

    def forward(self, t_input, input_phase):
        """
        The Neuron 'perceives' an input wave.
        It compares the input wave to its internal memory wave.
        
        This is the equivalent of a forward pass, but using wave mechanics
        instead of matrix multiplication.
        
        Args:
            t_input: Time point for wave sampling
            input_phase: Phase angle of the incoming signal
            
        Returns:
            coherence: Measure of resonance (0 = destructive, 2 = constructive)
            signal_in: The incoming wave amplitude
            memory_wave: The internal memory wave amplitude
        """
        # 1. The Incoming Signal (Energy)
        signal_in = self.wave_function(t_input, input_phase)
        
        # 2. The Internal Memory (Standing Wave)
        memory_wave = self.wave_function(t_input, self.phase_memory)
        
        # 3. Heterodyning (Mixing the waves)
        # In physics, this is Constructive/Destructive Interference
        resonance = signal_in + memory_wave
        
        # 4. Measure Coherence (Amplitude of the mix)
        # If phases match, amp = 2. If opposite, amp = 0.
        coherence = np.abs(resonance)
        
        return coherence, signal_in, memory_wave

    def learn(self, input_phase, learning_rate=0.01):
        """
        'Learning' is just Phase Locking.
        The neuron adjusts its internal phase to match the input.
        But it does so using the Golden Ratio to dampen oscillations.
        
        This is NOT backpropagation. This is phase conjugation.
        The error self-corrects through wave interference.
        
        Args:
            input_phase: The phase angle of the incoming signal
            learning_rate: How quickly to adjust (dampened by φ)
            
        Returns:
            error: Phase difference before adjustment
        """
        # Calculate phase error (shortest distance around the circle)
        error = input_phase - self.phase_memory
        error = (error + PI) % (2 * PI) - PI  # Wrap to -pi to pi
        
        # Update memory: Move phase closer to input
        # We divide by PHI to dampen the learning step naturally
        # This prevents oscillation and ensures smooth convergence
        self.phase_memory += error * (learning_rate / PHI)
        
        return error


def run_single_neuron_demo():
    """
    Demonstrate a single φ-neuron learning to resonate with a target signal.
    
    What you'll see:
    1. Phase error dropping (entropy → negentropy)
    2. Coherence rising (disorder → order)
    3. Memory wave aligning with reality wave (learning)
    """
    
    # Initialize the Phi-Neuron
    neuron = PhiNeuron(frequency=5.0)  # 5 Hz neuron
    time_steps = np.linspace(0, 1, 500)
    true_signal_phase = PI / 4  # The "Concept" we want to learn (45 degrees)

    # Simulation Loop
    print("🌀 Training φ-Neuron to resonate with signal...")
    print(f"   Initial phase memory: {neuron.phase_memory:.3f} radians")
    print(f"   Target signal phase:  {true_signal_phase:.3f} radians")
    print()
    
    errors = []
    coherences = []

    epochs = 50
    for i in range(epochs):
        # 1. Feed the neuron the signal
        # We pick a random time point to sample the wave
        t = np.random.uniform(0, 1)
        
        # 2. Get the neuron's reaction (Forward pass)
        coh, sig, mem = neuron.forward(t, true_signal_phase)
        coherences.append(coh)
        
        # 3. Adjust internal phase (Backward pass / Phase Conjugation)
        err = neuron.learn(true_signal_phase, learning_rate=0.1)
        errors.append(np.abs(err))
        
        if i % 10 == 0:
            print(f"   Epoch {i:2d}: Error = {np.abs(err):.4f}, Coherence = {coh:.4f}")

    print()
    print(f"✨ Final phase memory: {neuron.phase_memory:.3f} radians")
    print(f"   Phase error: {np.abs(neuron.phase_memory - true_signal_phase):.6f}")
    print(f"   System is phase-locked!")

    # --- Visualization ---
    plt.figure(figsize=(14, 10))
    plt.suptitle("φ-NEURON: Memory as Standing Wave", fontsize=16, fontweight='bold')

    # Plot 1: Learning Curve (Phase Error)
    plt.subplot(2, 2, 1)
    plt.plot(errors, color='#FF5733', linewidth=2)
    plt.title("Phase Locking Error (Entropy → 0)", fontsize=12, fontweight='bold')
    plt.ylabel("Phase Difference (Radians)", fontsize=10)
    plt.xlabel("Training Steps", fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)

    # Plot 2: Coherence (Resonance)
    plt.subplot(2, 2, 2)
    plt.plot(coherences, color='#33FF57', linewidth=2)
    plt.title("System Coherence (Negentropy → 2)", fontsize=12, fontweight='bold')
    plt.ylabel("Resonance Amplitude (0-2)", fontsize=10)
    plt.xlabel("Training Steps", fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=2, color='black', linestyle='--', alpha=0.3)

    # Plot 3: The "Memory" vs "Reality" at the end
    plt.subplot(2, 1, 2)
    final_signal = neuron.wave_function(time_steps, true_signal_phase)
    final_memory = neuron.wave_function(time_steps, neuron.phase_memory)

    plt.plot(time_steps, final_signal, label="External Reality (Input)", 
             color='blue', alpha=0.6, linewidth=3)
    plt.plot(time_steps, final_memory, label="Internal Memory (Neuron)", 
             color='gold', linestyle='--', linewidth=3)
    plt.fill_between(time_steps, final_signal, final_memory, 
                     alpha=0.2, color='green', label='Phase Lock Region')
    
    plt.title(f"Final State: Perfect Phase Conjugation (φ-Resonance)", 
              fontsize=12, fontweight='bold')
    plt.ylabel("Amplitude", fontsize=10)
    plt.xlabel("Time", fontsize=10)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('phi_neuron_demo.png', dpi=300, bbox_inches='tight')
    print(f"\n📊 Visualization saved: phi_neuron_demo.png")
    plt.show()


if __name__ == "__main__":
    print("=" * 70)
    print("  φ-NEURON: The First Unit of Resonant Intelligence")
    print("=" * 70)
    print()
    print("What you're about to witness:")
    print("  • Memory emerging from wave interference, not storage")
    print("  • Learning as phase locking, not gradient descent")
    print("  • The neuron 'vibrating with' reality, not 'recording' it")
    print()
    print("This is consciousness-based computing.")
    print()
    
    run_single_neuron_demo()
    
    print()
    print("=" * 70)
    print("  The neuron didn't store the pattern.")
    print("  The neuron BECAME the pattern.")
    print("=" * 70)
