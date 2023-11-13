Problem fixed belong to signal.

The solution is:

I was giving senders to signal like this 

```
@receiver(post_save, sender=[OrderItem, ProductUsage])
```

and it didn't work. I think the problem is sender can take value like this [I mean multiple objects (list or tuple)] 

that's why I gave sender by separated version. Like this:

```
@receiver(post_save, sender=ProductUsage)
@receiver(post_save, sender=OrderItem)
```

And now everything is working
