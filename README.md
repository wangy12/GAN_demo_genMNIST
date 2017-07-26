## An example of GAN

---

Using GAN to generate MNIST-like images

[//]: # (Image References)

[image1]: ./generate.png "generated MNIST-like images"
[image2]: ./inspect.png "results in the process of training"
[image3]: ./loss.png
[image4]: ./samples.png "samples from the last epoch"

---

Generator: Leaky ReLU, Tanh

Discriminator: Leaky ReLU, Sigmoid

---

### Results:

#### Training:

![alt text][image3]



#### Visualization: 

Samples from the last epoch (60th)

![alt text][image4]

Generated images in the process of training

![alt text][image2]

Generated MNIST-like images using the generator

![alt text][image1]

---

### Ref

[This Github repo](https://github.com/NELSONZHAO/zhihu/tree/master/mnist_gan)

---

Training ...
Epoch 1/100... Discriminator Loss: 0.0308(Real: 0.0070 + Fake: 0.0237)... Generator Loss: 3.6194

Epoch 2/100... Discriminator Loss: 0.2927(Real: 0.1254 + Fake: 0.1673)... Generator Loss: 5.0361

Epoch 3/100... Discriminator Loss: 3.9419(Real: 1.1667 + Fake: 2.7752)... Generator Loss: 1.9824

Epoch 4/100... Discriminator Loss: 1.1561(Real: 0.8688 + Fake: 0.2873)... Generator Loss: 3.3170

Epoch 5/100... Discriminator Loss: 1.2585(Real: 0.3231 + Fake: 0.9354)... Generator Loss: 2.1388

Epoch 6/100... Discriminator Loss: 1.8270(Real: 1.3464 + Fake: 0.4806)... Generator Loss: 1.1824

Epoch 7/100... Discriminator Loss: 0.9541(Real: 0.3897 + Fake: 0.5643)... Generator Loss: 1.2965

Epoch 8/100... Discriminator Loss: 0.9699(Real: 0.3727 + Fake: 0.5972)... Generator Loss: 1.7481

Epoch 9/100... Discriminator Loss: 1.8492(Real: 1.0346 + Fake: 0.8146)... Generator Loss: 2.8098

Epoch 10/100... Discriminator Loss: 2.2315(Real: 0.8212 + Fake: 1.4102)... Generator Loss: 0.8969

Epoch 11/100... Discriminator Loss: 0.4310(Real: 0.2284 + Fake: 0.2026)... Generator Loss: 2.7929

Epoch 12/100... Discriminator Loss: 2.5746(Real: 1.1192 + Fake: 1.4554)... Generator Loss: 0.7880

Epoch 13/100... Discriminator Loss: 0.8288(Real: 0.3962 + Fake: 0.4326)... Generator Loss: 1.9010

Epoch 14/100... Discriminator Loss: 1.1605(Real: 0.8729 + Fake: 0.2877)... Generator Loss: 2.4523

Epoch 15/100... Discriminator Loss: 1.6224(Real: 0.6026 + Fake: 1.0198)... Generator Loss: 1.0187

Epoch 16/100... Discriminator Loss: 1.2470(Real: 0.7247 + Fake: 0.5222)... Generator Loss: 1.6389

Epoch 17/100... Discriminator Loss: 1.3717(Real: 0.8167 + Fake: 0.5550)... Generator Loss: 2.1126

Epoch 18/100... Discriminator Loss: 1.0314(Real: 0.6542 + Fake: 0.3772)... Generator Loss: 1.7157

Epoch 19/100... Discriminator Loss: 0.9322(Real: 0.3342 + Fake: 0.5980)... Generator Loss: 1.3578

Epoch 20/100... Discriminator Loss: 0.8935(Real: 0.4314 + Fake: 0.4622)... Generator Loss: 1.7900

Epoch 21/100... Discriminator Loss: 0.6445(Real: 0.2747 + Fake: 0.3697)... Generator Loss: 2.1332

Epoch 22/100... Discriminator Loss: 0.9065(Real: 0.4548 + Fake: 0.4516)... Generator Loss: 1.5350

Epoch 23/100... Discriminator Loss: 0.4458(Real: 0.2658 + Fake: 0.1800)... Generator Loss: 2.1820

Epoch 24/100... Discriminator Loss: 0.6049(Real: 0.3459 + Fake: 0.2591)... Generator Loss: 2.8175

Epoch 25/100... Discriminator Loss: 0.6961(Real: 0.2597 + Fake: 0.4364)... Generator Loss: 2.3134

Epoch 26/100... Discriminator Loss: 1.0955(Real: 0.5509 + Fake: 0.5446)... Generator Loss: 1.6029

Epoch 27/100... Discriminator Loss: 1.0228(Real: 0.5027 + Fake: 0.5201)... Generator Loss: 1.6396

Epoch 28/100... Discriminator Loss: 0.6015(Real: 0.2216 + Fake: 0.3800)... Generator Loss: 1.7027

Epoch 29/100... Discriminator Loss: 0.8048(Real: 0.4366 + Fake: 0.3683)... Generator Loss: 1.7577

Epoch 30/100... Discriminator Loss: 0.9343(Real: 0.6657 + Fake: 0.2686)... Generator Loss: 2.0895

Epoch 31/100... Discriminator Loss: 1.0567(Real: 0.3963 + Fake: 0.6604)... Generator Loss: 1.3543

Epoch 32/100... Discriminator Loss: 1.0134(Real: 0.3752 + Fake: 0.6382)... Generator Loss: 1.2551

Epoch 33/100... Discriminator Loss: 1.0025(Real: 0.6246 + Fake: 0.3779)... Generator Loss: 1.5556

Epoch 34/100... Discriminator Loss: 1.0957(Real: 0.3894 + Fake: 0.7063)... Generator Loss: 1.1095

Epoch 35/100... Discriminator Loss: 0.8100(Real: 0.5790 + Fake: 0.2310)... Generator Loss: 2.1119

Epoch 36/100... Discriminator Loss: 0.9131(Real: 0.6156 + Fake: 0.2975)... Generator Loss: 2.0496

Epoch 37/100... Discriminator Loss: 1.1724(Real: 0.5946 + Fake: 0.5778)... Generator Loss: 1.5604

Epoch 38/100... Discriminator Loss: 0.8913(Real: 0.4593 + Fake: 0.4319)... Generator Loss: 1.6009

Epoch 39/100... Discriminator Loss: 0.9013(Real: 0.4504 + Fake: 0.4509)... Generator Loss: 1.8775

Epoch 40/100... Discriminator Loss: 0.7336(Real: 0.2834 + Fake: 0.4502)... Generator Loss: 1.5347

Epoch 41/100... Discriminator Loss: 1.1078(Real: 0.4435 + Fake: 0.6643)... Generator Loss: 1.2246

Epoch 42/100... Discriminator Loss: 0.9351(Real: 0.4022 + Fake: 0.5329)... Generator Loss: 1.4088

Epoch 43/100... Discriminator Loss: 0.9123(Real: 0.4067 + Fake: 0.5055)... Generator Loss: 1.4279

Epoch 44/100... Discriminator Loss: 0.8442(Real: 0.4288 + Fake: 0.4154)... Generator Loss: 1.5558

Epoch 45/100... Discriminator Loss: 1.1493(Real: 0.4684 + Fake: 0.6809)... Generator Loss: 1.0737

Epoch 46/100... Discriminator Loss: 1.1670(Real: 0.4984 + Fake: 0.6686)... Generator Loss: 1.1765

Epoch 47/100... Discriminator Loss: 0.8404(Real: 0.5508 + Fake: 0.2896)... Generator Loss: 1.8635

Epoch 48/100... Discriminator Loss: 1.2231(Real: 0.4925 + Fake: 0.7307)... Generator Loss: 1.0448

Epoch 49/100... Discriminator Loss: 0.9967(Real: 0.7037 + Fake: 0.2930)... Generator Loss: 1.9227

Epoch 50/100... Discriminator Loss: 0.9110(Real: 0.5509 + Fake: 0.3601)... Generator Loss: 1.5013

Epoch 51/100... Discriminator Loss: 0.9203(Real: 0.4803 + Fake: 0.4400)... Generator Loss: 1.3476

Epoch 52/100... Discriminator Loss: 1.0187(Real: 0.3823 + Fake: 0.6364)... Generator Loss: 1.1751

Epoch 53/100... Discriminator Loss: 0.8327(Real: 0.2831 + Fake: 0.5496)... Generator Loss: 1.2740

Epoch 54/100... Discriminator Loss: 0.7710(Real: 0.4835 + Fake: 0.2875)... Generator Loss: 1.7701

Epoch 55/100... Discriminator Loss: 0.9691(Real: 0.5141 + Fake: 0.4550)... Generator Loss: 1.5913

Epoch 56/100... Discriminator Loss: 0.8037(Real: 0.4165 + Fake: 0.3872)... Generator Loss: 1.6488

Epoch 57/100... Discriminator Loss: 1.0342(Real: 0.4619 + Fake: 0.5724)... Generator Loss: 1.5132

Epoch 58/100... Discriminator Loss: 0.7866(Real: 0.3543 + Fake: 0.4324)... Generator Loss: 1.5136

Epoch 59/100... Discriminator Loss: 0.8054(Real: 0.4113 + Fake: 0.3941)... Generator Loss: 1.6567

Epoch 60/100... Discriminator Loss: 1.2121(Real: 0.6551 + Fake: 0.5570)... Generator Loss: 1.3384

Epoch 61/100... Discriminator Loss: 1.0123(Real: 0.4811 + Fake: 0.5312)... Generator Loss: 1.3538

Epoch 62/100... Discriminator Loss: 0.8678(Real: 0.4112 + Fake: 0.4565)... Generator Loss: 1.4913

Epoch 63/100... Discriminator Loss: 1.2306(Real: 0.5982 + Fake: 0.6324)... Generator Loss: 1.0986

Epoch 64/100... Discriminator Loss: 0.8354(Real: 0.4954 + Fake: 0.3400)... Generator Loss: 1.5415

Epoch 65/100... Discriminator Loss: 0.9189(Real: 0.5246 + Fake: 0.3943)... Generator Loss: 1.5522

Epoch 66/100... Discriminator Loss: 0.7630(Real: 0.2840 + Fake: 0.4790)... Generator Loss: 1.3012

Epoch 67/100... Discriminator Loss: 1.2089(Real: 0.5630 + Fake: 0.6459)... Generator Loss: 1.4696

Epoch 68/100... Discriminator Loss: 1.1863(Real: 0.4265 + Fake: 0.7598)... Generator Loss: 0.9738

Epoch 69/100... Discriminator Loss: 0.7751(Real: 0.3776 + Fake: 0.3975)... Generator Loss: 1.5357

Epoch 70/100... Discriminator Loss: 0.8155(Real: 0.3470 + Fake: 0.4685)... Generator Loss: 1.3878

Epoch 71/100... Discriminator Loss: 1.0303(Real: 0.5511 + Fake: 0.4791)... Generator Loss: 1.5246

Epoch 72/100... Discriminator Loss: 0.8128(Real: 0.2804 + Fake: 0.5324)... Generator Loss: 1.2403

Epoch 73/100... Discriminator Loss: 0.8963(Real: 0.5933 + Fake: 0.3030)... Generator Loss: 1.7615

Epoch 74/100... Discriminator Loss: 0.7461(Real: 0.3886 + Fake: 0.3575)... Generator Loss: 1.5492

Epoch 75/100... Discriminator Loss: 1.0556(Real: 0.4487 + Fake: 0.6069)... Generator Loss: 1.1153

Epoch 76/100... Discriminator Loss: 0.8732(Real: 0.4711 + Fake: 0.4021)... Generator Loss: 1.4495

Epoch 77/100... Discriminator Loss: 1.0593(Real: 0.6200 + Fake: 0.4393)... Generator Loss: 1.5734

Epoch 78/100... Discriminator Loss: 0.9662(Real: 0.5341 + Fake: 0.4321)... Generator Loss: 1.5150

Epoch 79/100... Discriminator Loss: 0.8908(Real: 0.5912 + Fake: 0.2997)... Generator Loss: 1.6800

Epoch 80/100... Discriminator Loss: 0.9047(Real: 0.4259 + Fake: 0.4789)... Generator Loss: 1.3007

Epoch 81/100... Discriminator Loss: 0.9049(Real: 0.4255 + Fake: 0.4794)... Generator Loss: 1.3820

Epoch 82/100... Discriminator Loss: 0.7315(Real: 0.3582 + Fake: 0.3732)... Generator Loss: 1.5510

Epoch 83/100... Discriminator Loss: 0.7597(Real: 0.3871 + Fake: 0.3726)... Generator Loss: 1.5538

Epoch 84/100... Discriminator Loss: 0.8538(Real: 0.5481 + Fake: 0.3057)... Generator Loss: 1.6496

Epoch 85/100... Discriminator Loss: 0.7781(Real: 0.5187 + Fake: 0.2594)... Generator Loss: 1.8678

Epoch 86/100... Discriminator Loss: 0.7516(Real: 0.4093 + Fake: 0.3423)... Generator Loss: 1.7858

Epoch 87/100... Discriminator Loss: 0.8541(Real: 0.4862 + Fake: 0.3679)... Generator Loss: 1.5700

Epoch 88/100... Discriminator Loss: 1.0726(Real: 0.4964 + Fake: 0.5761)... Generator Loss: 1.2743

Epoch 89/100... Discriminator Loss: 0.9822(Real: 0.4144 + Fake: 0.5678)... Generator Loss: 1.3066

Epoch 90/100... Discriminator Loss: 0.7623(Real: 0.5079 + Fake: 0.2544)... Generator Loss: 1.8092

Epoch 91/100... Discriminator Loss: 1.1417(Real: 0.4316 + Fake: 0.7100)... Generator Loss: 1.0284


Epoch 92/100... Discriminator Loss: 1.0437(Real: 0.5409 + Fake: 0.5028)... Generator Loss: 1.1904

Epoch 93/100... Discriminator Loss: 1.2037(Real: 0.5657 + Fake: 0.6380)... Generator Loss: 1.1905

Epoch 94/100... Discriminator Loss: 0.8444(Real: 0.4486 + Fake: 0.3958)... Generator Loss: 1.5148

Epoch 95/100... Discriminator Loss: 0.8834(Real: 0.4852 + Fake: 0.3982)... Generator Loss: 1.3385

Epoch 96/100... Discriminator Loss: 0.8744(Real: 0.4112 + Fake: 0.4633)... Generator Loss: 1.2396

Epoch 97/100... Discriminator Loss: 1.1250(Real: 0.5876 + Fake: 0.5375)... Generator Loss: 1.1512

Epoch 98/100... Discriminator Loss: 0.9969(Real: 0.5388 + Fake: 0.4581)... Generator Loss: 1.5220

Epoch 99/100... Discriminator Loss: 0.9319(Real: 0.4412 + Fake: 0.4907)... Generator Loss: 1.2224

Epoch 100/100... Discriminator Loss: 0.8822(Real: 0.4370 + Fake: 0.4451)... Generator Loss: 1.4392
