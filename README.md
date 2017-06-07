Annotation Guidelines
=====================

Format of Data
--------------
Title <br />
Source (link to post for reference) <br />
Original post, root replies <br />
Thread (including OP and RR) <br />

```xml
<thread ID="xxx">
<OP author="xxx"> xxx </OP>
<reply author="xxx"> xxx </reply>
```

Argumentation tags 
------------------

An argument is the justification provided by the speaker/writer in support of a claim which is not self-evident. Arguments are put forward by speakers/writers in order to persuade hearers/readers to agree about the truth of a certain claim. 

**Claims**: stances expressed by a speaker on a certain matter. They can express predictions (e.g. “I think that the left wing will win the elections”), interpretations (“Probably John went home”), evaluations (e.g. “Your choice is a bad one”) as well as agreement/disagreement with other people’s claims (“I think you are totally wrong”/ “I agree”).  Note that in the latter case, it is frequent to find concessive statements of the type  “I agree with you that the environmental consequences are bad, but I still think that […]” where the speaker at the same time agrees and disagrees with other people’s claims. In those cases the proposition expressing agreement and that expressing sort of disagreement should be annotated as two separate claims. 

Claims can be expressed in one of 5 ways: agreement, disagreement, evaluation (rational or emotional), and interpretation.

* **interpretation**: the claim expresses predictions or explanations of states of affairs, i.e.  "I think he will win the election." or "He probably went home."
* **evaluation**: the claim expresses a more or less positive or negative judgement. Drawing from the distinction made in sentiment analysis and opinion mining, evaluations are sub-classified as: 
  * **evaluation-rational**: the claim expresses an opinion based on rational reasoning, non-subjective evidence or credible sources, i.e. "His political program is very solid." or "He is a very smart student."
  * **evaluation-emotional**: the claim expresses an opinion based on emotional reasons and/or subjective beliefs, i.e.  "Going to the gym is an unpleasant activity." or "I do not like doing yoga."
* **agreement** or **disagreement**: claims express that the speaker shares/does not share to a certain degree the beliefs held by another speaker, i.e. "I agree that going to the gym is boring" or "you are right" or "I do not think that he went home." or "You are not logically wrong." or "I don’t like your ideas." or "It may be true."

**Premises**: justifications provided by the speaker in support of a claim to persuade the audience of the validity of the claim. Like claims they can express opinions but their function is not that of introducing a new stance, but that of supporting one previously expressed. 

Arguments can exploit 3 modes of persuasion: logos, pathos and ethos. 

* **Logos**: the argument appeals to the use of reasonings which sound rational (e.g. <claim>He will probably win the elections </claim>”. <logos>He is  the favorite one according to the polls </logos>”) 

* **Pathos**: the argument aims at putting the audience in a certain frame of mind, appealing to emotions, or more generally touching upon topics in which the audience can somehow identify (e.g. “The spread of antibiotics is a threaten for the next generation”; “ the feeling of being home is unforgettable”). 

* **Ethos**: the argument appeals to the credibility of the author which can depend on his expertise in a certain field (e.g. “I am a chemical engineer”/ “I have been working in construction since I was a teenager”) as well as his title (“e.g. John is a Nobel Prize”) or his reputation (e.g. “According to John, who has been appointed by the New York Times one of the best journalist of the century….”). 

Notes: 
1. The unit of annotation is the proposition. Note that when two propositions are linked by a connectives (but, because and so on), the connective is not part of the labeling:
i.e. “<claim> everybody should eat at least one fruit a day</claim>  because <logos> it is healthy</logos>” 

2. Completely untagged sections mostly contain fluff (ex: greetings).

3. Both claims and arguments can be expressed by sentences at the interrogative form in presence of rhetorical questions – questions that are not meant to require an answer, which is obvious, but to lay emphasis on a state of affairs. Their function as claims/arguments has, thus, to be decided in context: e.g.  “<claim> Isn’t it great that we have no control on our private information being spread on social media? </claim>”. “<claim> We should fight for our privacy on the Web </claim>. <pathos> Don’t you love that  Google knows your favorite brand of shoes? </pathos>” .

4. Sometimes the main claim is in the title and the text immediately starts with an argument.  In this case we do not mark the title as claim.

Example
-------
```xml
<?xml version="1.0"?>
<thread ID="2rmwcd">
<title>CMV: Freedom of speech is being taken too far</title>
<source>http://www.reddit.com/r/changemyview/comments/2rmwcd/cmv_freedom_of_speech_is_being_taken_too_far/</source>
<OP author="5skandas">
In the last few weeks we've had two huge events happen in the world, both of which were caused by matters relating 
to "freedom of speech." The first being the hacking of Sony over The Interview, and today the shooting at the 
offices of a satirical magazine in Paris. <claim> I certainly value our free speech </claim> but <claim> to me 
there is a clear line between exercising your first amendment right (<premise> "President Obama sucks!" etc 
</premise>) and doing things that are known to be offensive to other cultures (<premise> Satirical cartoons of 
prophets, assassinating leaders, etc </premise>). </claim>

<claim> Perhaps this is a bad analogy </claim> - but <premise> if you say something antagonizing to a bully and 
you get your ass kicked, you should have anticipated that outcome. </premise>

</OP>

<reply id="cnhc295" author="Grunt08">
&gt; Perhaps this is a bad analogy - but if you say something antagonizing to a bully and you get your ass 
kicked, you should have anticipated that outcome.

<premise> Think of something you do every day that you consider perfectly reasonable; something that harms 
nobody in any direct sense </premise>. <premise>  Let's imagine this thing is to defined as "walking down the 
street wearing headphones" </premise>.

<premise> Now imagine that I tell you that you doing this offends me deeply for reasons of personal 
belief that you don't share. </premise> <premise> I warn you that continuing to do this will mean that I 
will shoot you on sight. </premise>

<claim> In a society that can't protect you from me, it might be *wise* for you to take off your headphones to 
preserve your life </claim>. <premise> That does not make my demand legitimate </premise>, <premise> does not 
make my shooting you an acceptable act </premise> and <premise> does not make my actions your fault </premise>. 
<premise> What you ought to hope is that society will protect you from someone like me and make it clear to me 
that my preferences will not be especially entertained because I threaten violence. </premise>

<claim> I think people who satirize Muhammad in ways that Muslims consider blasphemous should stop doing that. 
</claim> <claim> I think it's counterproductive, antagonizing and in poor taste. </claim>  But <premise> if 
someone disagrees with me on that point, *they don't deserve to be shot.* </premise>

</reply>

[...]

<reply id="cnhm4xd" author="5skandas">
&gt; North Korea hacked Sony because they are so paranoid and insecure that they can't stand their 
leader being mocked. Some Muslims are so irrationally offended and self-important that they believe they have 
both the imperative and the right to kill people for drawing pictures. Neither of these examples illustrate 
problems with the speakers, they show the unhinged reactions of listeners. 

Damn. I think you just changed my view. That's what I needed, thank you. ∆
</reply>
```
