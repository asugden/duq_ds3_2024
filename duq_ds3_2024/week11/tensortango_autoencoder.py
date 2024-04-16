from duq_ds3_2024.week4 import read_wine_data
from duq_ds3_2024.week11.tensortango import train, layer, mlp


df = read_wine_data.read()
labels = df['quality']
features = df[[col for col in df.columns if col != 'quality']]

# Min max scaling-- maybe you want to 
for col in features:
    features[col] -= features[col].min()
    features[col] /= features[col].max() # equivalent to features[col] = features[col]/

neural_net = mlp.MLP([layer.Relu(11, 8),
                      layer.Relu(8, 6),
                      layer.Relu(6, 4),
                      layer.Tanh(4, 2),
                      layer.Relu(2, 4),
                      layer.Relu(4, 6),
                      layer.Relu(6, 8),
                      layer.Relu(8, 11)])
train.train(neural_net, features.values, features.values)
print(neural_net.forward(features.values))