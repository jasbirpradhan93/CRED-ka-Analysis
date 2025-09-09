"""Helper functions for CRED SWOT Analysis."""
import matplotlib.pyplot as plt

def plot_swot_quadrant(strengths, weaknesses, opportunities, threats, save_path=None):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')

    # Plot text in quadrants
    ax.text(-0.5, 0.5, "\n".join(strengths), ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.5", fc="lightgreen", alpha=0.5))
    ax.text(0.5, 0.5, "\n".join(opportunities), ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.5", fc="lightblue", alpha=0.5))
    ax.text(-0.5, -0.5, "\n".join(weaknesses), ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.5", fc="salmon", alpha=0.5))
    ax.text(0.5, -0.5, "\n".join(threats), ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.5", fc="khaki", alpha=0.5))

    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.axis('off')
    plt.title("CRED SWOT Quadrant", fontsize=14)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()
