"""Create the framework for training our neural network"""

from duq_ds3_2024.week11.tensortango import loss, mlp, optimizer, tensor, data_iterator


def train(neural_net: mlp.MLP,
          features: tensor.Tensor,
          labels: tensor.Tensor,
          epochs: int = 5000,
          iterator = data_iterator.BatchIterator(),
          loss_fn = loss.MSE(),
          optimizer_obj = optimizer.SGD,
          learning_rate: float = 0.05):
    """Train a neural network, otherwise known as a multilayer 
    perceptron or fully connected feedforward network.

    Args:
        neural_net (mlp.MLP): a defined neural network
        features (tensor.Tensor): _description_
        labels (tensor.Tensor): _description_
        epochs (int, optional): number of rounds of forward/backward 
            training. Defaults to 5000.
        iterator (_type_, optional): batch iterator. 
            Defaults to data_iterator.BatchIterator.
        loss_fn (_type_, optional): loss function. Defaults to loss.MSE.
        optimizer_obj (_type_, optional): the mechanism that updates
            the learning rate. Defaults to optimizer.SGD.
        learning_rate (float, optional): the amount of error to include
            in each backprop step. Defaults to 0.05.
    """
    optim = optimizer_obj(neural_net, learning_rate)
    for epoch in range(epochs):
        epoch_loss = 0.0
        for batch in iterator(features, labels):
            features, labels = batch
            predictions = neural_net.forward(features)  # the first result is features
            epoch_loss =+ loss_fn.loss(predictions, labels)  # batch[1] is labels
            grad = loss_fn.grad(predictions, labels)
            neural_net.backward(grad)
            optim.step()
            neural_net.zero_parameters()
        print(f'Epoch {epoch} has loss {epoch_loss}')


if __name__ == '__main__':
    import numpy as np
    from duq_ds3_2024.week11.tensortango import layer

    # Use XOR because linear functions cannot represent XOR
    features = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    # Labels are going to be values of true and values of false
    labels = np.array([
        [1, 0],  # false is 1, true is 0
        [0, 1],  # T
        [0, 1],  # T
        [1, 0]  # F
        ])
    
    neural_net = mlp.MLP([layer.Tanh(2, 2),
                          layer.Tanh(2, 2)])
    train(neural_net, features, labels)
    print(neural_net.forward(features))