import operator

first="The Seven Traits Of Change-Readiness\n\nUnderstanding Your Scores\n\nYour overall score:"
second="\n\n\nOptional range for all categories is between 154 and 182\n\nScores too low may mean you are not open to change and consequently it may take longer for you to transition through change missing out on opportunities. Score too high may mean you are restless and may not stick with a change long enough to see the full results.\n\nOptimal range for each category is between 22 and 26"
third="\nResourceful people are effective at taking the most of any situation and utilizing whatever resources are available to develop plans and contingencies. They see more than one way to achieve a goal, and they're able to look in less obvious places to find help. They have a real talent for creating new ways to solve old problems.\n\nWhen people low in resourcefulness encounter obstacles, they get stuck, dig in their heels, and go back to the old way. Very high scorers (over 26) might overlook obvious solutions and create more work than is necessary.\n\nOptimism: "
fourth="\nIs the glass half empty or half full? Optimism is highly correlated with Change-Readiness, since the pessimist observes only problems and obstacles while the optimist recognizes opportunities and possibilities.\n\nOptimists tend to be more enthusiastic and positive about change. Their positive outlook is, founded on an abiding faith in the future and the belief that things usually work out for the best. Very high optimism scorers (over 26) may lack critical-thinking skills.\n\nAdventurousness: "
fifth="\nTwo ingredients capture this adventurous spirit: the inclination to take risks and the desire to pursue the unknown, to walk the path less taken. Adventurous people love a challenge.\nSince change always involves both risk and the unknown, they usually perform well during organizational shake-ups. They are the proactors, the employees who initiate and create change. But very high scores (over 26) may indicate a tendency toward recklessness.\n\nPassion / Drive: "
sixth="\nPassion is the fuel that maximizes all the other traits. If you have passion, nothing appears impossible. If you don't, change is exhausting. Passion is the individual's level of personal dynamism. It shows up in a person's level of intensity and determination.\n\nTo make a new procedure work, to overcome the myriad of problems that any plan for change unwittingly produces, you've got to have passion and enthusiasm. Very high scorers (over 26), however, may mean you're bullheaded, obsessed, and heading for burnout.\n\nAdaptability: "
seventh="\nAdaptability includes two elements: flexibility and resilience. Flexible people have goals and dreams like everyone else, but they're not overly invested in them. When something doesn't work out, they'll say, 'Plan A doesn't work, let's go to Plan B.' Resilience is the capacity to rebound from adversity quickly with a minimum of trauma. Failure or mistakes do not throw them. They don't dwell on them and get depressed but bounce back quickly and move on.\n\n\nHigh scorers on this trait are not wedded to specific outcomes. If the situation changes, their expectations shift right along with it. Scoring too high (over 26) in this trait indicates a lack of commitment or stick-to-it-ness.\n\nConfidence: "
eighth="\nIf optimism is the view that a situation will work out, confidence is the belief in your own ability to handle it. There is situational confidence - 'I know I can swim across this channel, learn this program, write this report' - and self-confidence - 'I can handle whatever comes down the pike.' Self-confidence is the kind of confidence the Change Readiness Scale measures.\n\nHigh scorers are generally individuals with a strong sense of self-esteem. But more specifically, they believe they can make any situation work for them. Scorers above 26 may indicate a cocky, know-it-all attitude and lack of receptivity to feedback.\n\nTolerance for Ambiguity: "
ninth="\nThe one certainty surrounding change is that it spawns uncertainty. No matter how carefully you plan it, there is always an element of indefiniteness or ambiguity.\n\nWithout a healthy tolerance for ambiguity, change is not only uncomfortable; it's downright scary. But too much tolerance can also get you in trouble. You may have difficulty finishing tasks and making decisions. If you scored over 26 you fall in this category.\n\nYour Profile: You'll probably find you have higher scores on some traits and lower scores on others. This is typical of most profiles and indicates that some of your Change-Readiness traits are more developed than others."


def change_readyness_result(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35):
    resourcefulness = int(q6)+int(q13)+int(q20)+int(q27)+int(q34)
    adaptability = 35 - (int(q3)+int(q10)+int(q17)+int(q24)+int(q31))
    optimism =  35 - (int(q5)+int(q12)+int(q19)+int(q26)+int(q33))
    confidence =  int(q2)+int(q9)+int(q16)+int(q23)+int(q30)
    adventurousness = 35- (int(q1)+int(q8)+int(q15)+int(q22)+int(q29))
    tolerance = 35 - (int(q7)+int(q14)+int(q21)+int(q28)+int(q35))
    passion = int(q4)+int(q11)+int(q18)+int(q25)+int(q32)
    result = {
        "Resourcefulness":resourcefulness,
        "Adaptability":adaptability,
        "Optimism":optimism,
        "Confidence":confidence,
        "Adventurousness":adventurousness,
        "Tolerance for Ambiguity":tolerance,
        "Passion/Drive":passion
        }
    total = int(resourcefulness)+int(adaptability)+int(optimism)+int(confidence)+int(adventurousness)+int(tolerance)+int(passion)
    best = "\n\nYour strongest trait is: "+max(result.items(), key=operator.itemgetter(1))[0]+'\n\nResourcefulness: '
    f = open('sample.txt', 'w')
    f.write(first+str(total)+second+best+str(result["Resourcefulness"])+third
            +str(result["Adaptability"])+fourth+str(result["Adventurousness"])
            +fifth+str(result["Passion/Drive"])+sixth+str(result["Adaptability"])+seventh
            +str(result["Confidence"])+eighth+str(result["Tolerance for Ambiguity"])+ninth)
    body = (first+str(total)+second+best+str(result["Resourcefulness"])+third
            +str(result["Adaptability"])+fourth+str(result["Adventurousness"])
            +fifth+str(result["Passion/Drive"])+sixth+str(result["Adaptability"])+seventh
            +str(result["Confidence"])+eighth+str(result["Tolerance for Ambiguity"])+ninth)
    return body


a = change_readyness_result(4,2,1,3,4,5,2,6,2,4,5,3,1,2,3,5,1,4,5,6,5,6,1,2,3,2,1,2,3,4,5,2,3,5,6)
print(a)