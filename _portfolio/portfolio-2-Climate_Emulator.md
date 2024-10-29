---
title: "ResNet-based Climate Model Emulator"
excerpt: "What if we could reduce climate model computation from months to minutes?
<br>
<img src='/images/loss_plot.jpg' alt='Loss Plot' width='400' height='400' style='display: block; margin: 0 auto;'>"
collection: portfolio
---

Despite being the industry standard, numerical climate models are:
- slow (take months to run)
- computationally intensive (requiring 88 CPUs as a bare minimum)
- excessively complex (include hundreds of variables although most scientists are only interested in a few)

To address this issue, I've developed a ResNet-based model that emulates NASA's Global Climate Model for precipitation predictions. So far, I've:
- Achieved *state of the art* results (surpassing the best published result)
- Reduced computation time from ~2 months to 5 minutes

Although in early stages, this work has major implications for the role of deep learning in supplementing climate research.

<img src='/images/loss_plot.jpg' alt='Loss Plot' width='400' height='400' style='display: block; margin: 0 auto;'>
