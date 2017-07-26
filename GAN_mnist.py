import tensorflow as tf
import numpy as np
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", reshape=False)


def get_inputs(real_size, noise_size):
    """
    real image and noise image
    """
    real_img = tf.placeholder(tf.float32, [None, real_size], name='real_img')
    noise_img = tf.placeholder(tf.float32, [None, noise_size], name='noise_img')
    
    return real_img, noise_img
    
def get_generator(noise_img, n_units, out_dim, reuse=False, alpha=0.01):
    """   
    noise_img: input
    n_units: hidden layer units
    out_dim: size of output 32*32=784
    alpha: coefficient of leaky ReLU
    """
    with tf.variable_scope("generator", reuse=reuse):
        # hidden layer
        hidden1 = tf.layers.dense(noise_img, n_units)
        # leaky ReLU
        hidden1 = tf.maximum(alpha * hidden1, hidden1)
        # dropout
        hidden1 = tf.layers.dropout(hidden1, rate=0.2)

        # logits & outputs
        logits = tf.layers.dense(hidden1, out_dim)
        outputs = tf.tanh(logits)
        
        return logits, outputs

def get_discriminator(img, n_units, reuse=False, alpha=0.01):
        
    with tf.variable_scope("discriminator", reuse=reuse):
        # hidden layer
        hidden1 = tf.layers.dense(img, n_units)
        hidden1 = tf.maximum(alpha * hidden1, hidden1)
        
        # logits & outputs
        logits = tf.layers.dense(hidden1, 1)
        outputs = tf.sigmoid(logits)
        
        return logits, outputs


# define parameters
img_size = mnist.train.images[0].shape[0] * mnist.train.images[0].shape[1]
noise_size = 100
# number of hidden layer of generator
g_units = 128
# number of hidden layer of discriminator
d_units = 128
alpha = 0.01
learning_rate = 0.001
# label smoothing
smooth = 0.1


tf.reset_default_graph()

real_img, noise_img = get_inputs(img_size, noise_size)

# generator
g_logits, g_outputs = get_generator(noise_img, g_units, img_size)

# discriminator
d_logits_real, d_outputs_real = get_discriminator(real_img, d_units)
d_logits_fake, d_outputs_fake = get_discriminator(g_outputs, d_units, reuse=True)

# LOSS
# loss of discriminator
# real image -- 1
d_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_real, labels=tf.ones_like(d_logits_real)) * (1 - smooth))
# generated fake image -- 0
d_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.zeros_like(d_logits_fake)))
# sum of above
d_loss = tf.add(d_loss_real, d_loss_fake)

# loss of generator -- 1 (fake to be real)
g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.ones_like(d_logits_fake)) * (1 - smooth))

# Optimizer
train_vars = tf.trainable_variables()

# generator中的tensor
g_vars = [var for var in train_vars if var.name.startswith("generator")]
# discriminator中的tensor
d_vars = [var for var in train_vars if var.name.startswith("discriminator")]

# optimizer
d_train_opt = tf.train.AdamOptimizer(learning_rate).minimize(d_loss, var_list=d_vars)
g_train_opt = tf.train.AdamOptimizer(learning_rate).minimize(g_loss, var_list=g_vars)


# TRAINING

batch_size = 64
epochs = 60
n_sample = 25

# restore
samples = []

losses = []

saver = tf.train.Saver(var_list = g_vars)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
        
    print("Training ...")
    
    for e in range(epochs):
        for batch_i in range(mnist.train.num_examples//batch_size):
            batch = mnist.train.next_batch(batch_size)
            
            #print(batch.shape())
            
            batch_images = batch[0].reshape((batch_size, img_size))
            # output of tanh ~ (-1,1)
            batch_images = batch_images*2 - 1
            
            # noise image -- input to generator
            batch_noise = np.random.uniform(-1, 1, size=(batch_size, noise_size))
            
            # Run optimizers
            _ = sess.run(d_train_opt, feed_dict={real_img: batch_images, noise_img: batch_noise})
            _ = sess.run(g_train_opt, feed_dict={noise_img: batch_noise})
        
        # loss of each epoch
        # total loss of distriminator
        train_loss_d = sess.run(d_loss, feed_dict = {real_img: batch_images, noise_img: batch_noise})
        # real img loss
        train_loss_d_real = sess.run(d_loss_real, feed_dict = {real_img: batch_images, noise_img: batch_noise})
        # fake img loss
        train_loss_d_fake = sess.run(d_loss_fake, feed_dict = {real_img: batch_images, noise_img: batch_noise})
        # generator loss
        train_loss_g = sess.run(g_loss, feed_dict = {noise_img: batch_noise})
        
            
        print("Epoch {}/{}...".format(e+1, epochs),
              "Discriminator Loss: {:.4f}(Real: {:.4f} + Fake: {:.4f})...".format(train_loss_d, train_loss_d_real, train_loss_d_fake),
              "Generator Loss: {:.4f}".format(train_loss_g))    
        
        losses.append((train_loss_d, train_loss_d_real, train_loss_d_fake, train_loss_g))
        
        sample_noise = np.random.uniform(-1, 1, size=(n_sample, noise_size))
        gen_samples = sess.run(get_generator(noise_img, g_units, img_size, reuse=True),
                               feed_dict={noise_img: sample_noise})
        samples.append(gen_samples)
        
        
        saver.save(sess, './checkpoints/generator.ckpt')

# Visualization
with open('train_samples.pkl', 'wb') as f:
    pickle.dump(samples, f)

fig, ax = plt.subplots(figsize=(20,7))
losses = np.array(losses)
plt.plot(losses.T[0], label='Discriminator Total Loss')
plt.plot(losses.T[1], label='Discriminator Real Loss')
plt.plot(losses.T[2], label='Discriminator Fake Loss')
plt.plot(losses.T[3], label='Generator')
plt.title("Training Losses")
plt.legend()
plt.savefig('loss')


# Load samples from generator taken while training
with open('train_samples.pkl', 'rb') as f:
    samples = pickle.load(f)

def view_samples(epoch, samples):

    fig, axes = plt.subplots(figsize=(7,7), nrows=5, ncols=5, sharey=True, sharex=True)
    for ax, img in zip(axes.flatten(), samples[epoch][1]): # samples[epoch][1]: image，[0]: logits
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        im = ax.imshow(img.reshape((28,28)), cmap='Greys_r')
    
    # plt.savefig('samples')
    return fig, axes
    
    
fig_sample, axes_sample = view_samples(-1, samples) # outputs of last epoch
plt.savefig('samples')


epoch_idx = [0, 5, 10, 20, 40, 59] # 80, 100, 150, 250
show_imgs = []
for i in epoch_idx:
    show_imgs.append(samples[i][1])
    
    
rows, cols = 6, 25
fig, axes = plt.subplots(figsize=(30,12), nrows=rows, ncols=cols, sharex=True, sharey=True)

idx = range(0, epochs, int(epochs/rows))

for sample, ax_row in zip(show_imgs, axes):
    for img, ax in zip(sample[::int(len(sample)/cols)], ax_row):
        ax.imshow(img.reshape((28,28)), cmap='Greys_r')
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        
plt.savefig('inspect')
        

saver = tf.train.Saver(var_list=g_vars)
with tf.Session() as sess:
    saver.restore(sess, tf.train.latest_checkpoint('checkpoints'))
    sample_noise = np.random.uniform(-1, 1, size=(25, noise_size))
    gen_samples = sess.run(get_generator(noise_img, g_units, img_size, reuse=True),
                           feed_dict={noise_img: sample_noise})
                           
fig_new, axes_new = view_samples(0, [gen_samples])
plt.savefig('generate')
