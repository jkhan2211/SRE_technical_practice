# Git Domain Questions

##### Question 1
How do you pass "message" when you commit your git code? 

##### Answer:
```
git commit -m "message"
```

##### Question 2
If you were to make a change for a commit done in 30 days ago with respect to a machine type used? 
How would you go about doing this change? 

Would you directly change it? 

##### Answer:
git clone -> branch -> github ui -> blame(history)
                                        # make your change


##### Question 2
What is branch protection in github? 

##### Answer:

[Working branch] ----->[repo(master/main)]

Branch protection, is there to allow collabration between team on a given repo
[main] - sync approach
we should make sure that branch that are raised there should be a PR, enable branch protection 
main is prod ready code

