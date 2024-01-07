import matplotlib.pyplot as plt
import numpy as np

def plot_accuracy(history, line_point=5, title='Training and Validation Accuracy Over Epochs', ax=None):
    epochs = len(history.history['accuracy'])
    x_labels = np.arange(1, epochs + 1)  # Start from 1
    if ax is None:
        ax = plt.gca()  # Use the current axis if not provided
    ax.plot(history.history['accuracy'], 'o-', label='Training Accuracy')
    ax.plot(history.history['val_accuracy'], 'o-', label='Validation Accuracy')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Accuracy')
    ax.set_xticks(range(epochs))
    ax.set_xticklabels(x_labels)  # from 1 to all
    ax.set_ylim([min(history.history['accuracy']) - 0.01, max(history.history['val_accuracy']) + 0.01])
    ax.legend(loc=0)  # optimal location
    ax.set_title(title)
    ax.axvline(x=line_point-1, color='red', linestyle='--', linewidth=0.7)  # Dotted line for the specified epoch

    #val_loss, val_accuracy = model.evaluate(val_ds)
    #print(f"Validation loss: {val_loss}")
    #print(f"Validation accuracy: {val_accuracy}")

    plt.savefig(f'{title.lower().replace(" ", "_")}_accuracy_plot.png', dpi=300, bbox_inches='tight')  # save image
########################################################################


