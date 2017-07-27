from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Base, Category, Book

engine = create_engine(
    'postgresql://catalog:catalog123@localhost/catalog')  # Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


user1 = User(name="Josue Acosta", email="acostajosued@gmail.com", picture="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg")
user2 = User(name="", email="ajosue046@gmail.com", picture="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg")
user3 = User(name="Josue Acosta", email="ajosue025@gmail.com", picture="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg")
user4 = User(name="", email="mejiafelicia18@gmail.com", picture="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg")
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()

category1 = Category(name="Science Fiction")
category2 = Category(name="Satire")
category3 = Category(name="Drama")
category4 = Category(name="Action And Adventure")
category5 = Category(name="Romance")
category6 = Category(name="Mystery")
category7 = Category(name="Horror")
category8 = Category(name="Self Help")
category9 = Category(name="Health")
category10 = Category(name="Guide")
category11 = Category(name="Travel")
category12 = Category(name="Children")
category13 = Category(name="Religion, Spirituality & New Age")
category14 = Category(name="Science")
category15 = Category(name="History")
category16 = Category(name="Business")
category17 = Category(name="Computers")
category18 = Category(name="Literacy")
category19 = Category(name="Urban")
category20 = Category(name="Comics & Graphic Novel")
category21 = Category(name="Biographies")
category22 = Category(name="Autobiographies")
category23 = Category(name="Journals")
category24 = Category(name="Memoirs")
category25 = Category(name="Trilogy")
category26 = Category(name="Art")


session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.add(category6)
session.add(category7)
session.add(category8)
session.add(category9)
session.add(category10)
session.add(category11)
session.add(category12)
session.add(category13)
session.add(category14)
session.add(category15)
session.add(category16)
session.add(category17)
session.add(category18)
session.add(category19)
session.add(category20)
session.add(category21)
session.add(category22)
session.add(category23)
session.add(category24)
session.add(category25)
session.add(category26)


session.commit()

book1 = Book(id=7,
             title="Dune",
             author="Frank Herbet",
             description="Dune tells the story of young Paul Atreides and House Atreides as they take over control of the desert planet Arrakis from their hated rivals House Harkonnen. Despite its harsh climate, unfriendly native population and hostile wildlife (i.e. Killer Worms), Arrankis is also the only known source in the universe of the “spice” Melange – an addictive substance which has the ability to extend life and give greater awareness to the user – including the ability to fold space-time for interstellar travel. Suffice it to say, the Spice is the engine that powers the entire Empire, making Arrakis the most strategically important planet in the universe.",
             category_name="Science Fiction",
             user_id=1)
book2 = Book(id=8,
             title="Foundation",
             author="Isaac Asimov",
             description="While it would be hard to call Foundation action-packed (most of the actual fighting and war takes place “off-screen”), there is just enough intrigue and suspense to keep the story humming along. But even though it has its entertaining elements, I would recommend this book to a friend as a novel of “Ideas.” Sometimes you’re just not ready to appreciate something like that at first (I wasn’t). But if you are, there are few better places to start than Asimov’s crowning achievement.",
             category_name="Science Fiction",
             user_id=1)
book3 = Book(id=9,
             title="Fahrenheit 451",
             author="Ray Bradbury",
             description="The novel takes place in a future in which reading has been outlawed by a population that values the pursuit of pleasure over knowledge. “Illegal” books are rounded up and burned by “Firemen” for the good of humanity (The title of the novel refers to the temperature at which book paper will burn). Our protagonist, Guy Montag, is a Fireman who begins to question the practice of book burning after an incident at the home of a woman whose books were going to be burned. After inadvertently reading a line in one of her books, he decides to steal the book. When the woman eventually allows herself to be burned alive along with all of her books, Guy begins to reconsider his belief that books have no value.As the novel progresses, Guy starts to become more and more obsessed with collecting and memorizing books and begins to find kindred spirits who have been actively trying to preserve as many books as they can (often going so far as to memorize their contents before burning them to avoid detection). At the same time, Guy’s superiors at the Fire department begin to suspect his book hoarding tendencies and eventually force him to burn his entire house to the ground. All of this takes place while newscasts warn of a pending war that is foreshadowed throughout the book.",
             category_name="Science Fiction",
             user_id=1)
book4 = Book(id=10,
             title="Hyperion",
             author="Dan Simmons",
             description="The structure of Hyperion mirrors that of Chaucer’s Canterbury Tales in its use of a pilgrimage as a framing device during which each of its main characters get a chance to tell their own unique story. The voyage is made up of seven pilgrims: the Priest, the Soldier, the Poet, the Scholar (and his daughter), the Detective and the Consul – each of whom have their own compelling back story that help give us an idea of why they chose to make the trip. The trip itself involves a pilgrimage to the distant planet of Hyperion in order to confront the legendary creature known as The Shrike (so named for its habit of impaling its victims on a tree of metal thorns). With the WorldWeb on the brink of war with a barbarian group of genetically altered humans called the Ousters, the pilgrims have been asked to make one last journey to the Time Tombs (ancients structures that move backwards through time) in order to learn the secret of the Shrike and hopefully help prevent the destruction of human civilization.",
             category_name="Science Fiction",
             user_id=2)
book5 = Book(id=11,
             title="Animal Farm",
             author="George Orwell",
             description="As ferociously fresh as it was more than a half century ago, this remarkable allegory of a downtrodden society of overworked, mistreated animals, and their quest to create a paradise of progress, justice, and equality is one of the most scathing satires ever published. As we witness the rise and bloody fall of the revolutionary animals, we begin to recognize the seeds of totalitarianism in the most idealistic organization; and in our most charismatic leaders, the souls of our cruelest oppressors.",
             category_name="Satire",
             user_id=2)
book6 = Book(id=12,
             title="Fight Club",
             author="Chuck Palahniuk",
             description="Every weekend, in basements and parking lots across the country, young men with good white-collar jobs and absent fathers take off their shoes and shirts and fight each other barehanded for as long as they have to. Then they go back to those jobs with blackened eyes and loosened teeth and the sense that they can handle anything. Fight Club is the invention of Tyler Durden, projectionist, waiter and dark, anarchic genius. And it's only the beginning of his plans for revenge on a world where cancer support groups have the corner on human warmth.",
             category_name="Satire",
             user_id=2)
book7 = Book(id=13,
             title="Romeo and Juliet",
             author="William Shakespeare",
             description="Romeo and Juliet is set in Verona, Italy, where there is an ongoing feud between the Montague and Capulet families. The play opens with servants from both houses engaged in a street brawl that eventually draws in the family patriarchs and the city officials, including Prince Escalus. The Prince ends the conflict by issuing a decree that prohibits any further fighting at the risk of great punishment.",
             category_name="Drama",
             user_id=3)
book8 = Book(id=14,
             title="The Da Vinci Code",
             author="Dan Brown",
             description="""An ingenious code hidden in the works of Leonardo da Vinci. A desperate race through the cathedrals and castles of Europe. An astonishing truth concealed for centuries . . . unveiled at last. While in Paris, Harvard symbologist Robert Langdon is awakened by a phone call in the dead of the night. The elderly curator of the Louvre has been murdered inside the museum, his body covered in baffling symbols. As Langdon and gifted French cryptologist Sophie Neveu sort through the bizarre riddles, they are stunned to discover a trail of clues hidden in the works of Leonardo da Vinci—clues visible for all to see and yet ingeniously disguised by the painter.

            Even more startling, the late curator was involved in the Priory of Sion—a secret society whose members included Sir Isaac Newton, Victor Hugo, and Da Vinci—and he guarded a breathtaking historical secret. Unless Langdon and Neveu can decipher the labyrinthine puzzle—while avoiding the faceless adversary who shadows their every move—the explosive, ancient truth will be lost forever.""",
             category_name="Mystery",
             user_id=4)
book9 = Book(id=15,
             title="The Hunger Games",
             author="Suzanne Collins",
             description="The nation of Panem, formed from a post-apocalyptic North America, is a country that consists of a wealthy Capitol region surrounded by 12 poorer districts. Early in its history, a rebellion led by a 13th district against the Capitol resulted in its destruction and the creation of an annual televised event known as the Hunger Games. In punishment, and as a reminder of the power and grace of the Capitol, each district must yield one boy and one girl between the ages of 12 and 18 through a lottery system to participate in the games. The 'tributes' are chosen during the annual Reaping and are forced to fight to the death, leaving only one survivor to claim victory.

            When 16-year-old Katniss's young sister, Prim, is selected as District 12's female representative, Katniss volunteers to take her place. She and her male counterpart Peeta, are pitted against bigger, stronger representatives, some of whom have trained for this their whole lives. , she sees it as a death sentence. But Katniss has been close to death before. For her, survival is second nature.",
             category_name="Trilogy",
             user_id=3)
book10 = Book(id=16,
             title="Catching Fire",
             author="Suzanne Collins",
             description="Against all odds, Katniss has won the Hunger Games. She and fellow District 12 tribute Peeta Mellark are miraculously still alive. Katniss should be relieved, happy even. After all, she has returned to her family and her longtime friend, Gale. Yet nothing is the way Katniss wishes it to be. Gale holds her at an icy distance. Peeta has turned his back on her completely. And there are whispers of a rebellion against the Capitol - a rebellion that Katniss and Peeta may have helped create.

            Much to her shock, Katniss has fueled an unrest she's afraid she cannot stop. And what scares her even more is that she's not entirely convinced she should try. As time draws near for Katniss and Peeta to visit the districts on the Capitol's cruel Victory Tour, the stakes are higher than ever. If they can't prove, without a shadow of a doubt, that they are lost in their love for each other, the consequences will be horrifying.

            In Catching Fire, the second novel in the Hunger Games trilogy, Suzanne Collins continues the story of Katniss Everdeen, testing her more than ever before...and surprising readers at every turn.",
             category_name="Trilogy",
             user_id=3)
book11 = Book(id=17,
             title="Mockingjay",
             author="Suzanne Collins",
             description="Katniss Everdeen, girl on fire, has survived, even though her home has been destroyed. Gale has escaped. Katniss's family is safe. Peeta has been captured by the Capitol. District 13 really does exist. There are rebels. There are new leaders. A revolution is unfolding.

            It is by design that Katniss was rescued from the arena in the cruel and haunting Quarter Quell, and it is by design that she has long been part of the revolution without knowing it. District 13 has come out of the shadows and is plotting to overthrow the Capitol. Everyone, it seems, has had a hand in the carefully laid plans--except Katniss.

            The success of the rebellion hinges on Katniss's willingness to be a pawn, to accept responsibility for countless lives, and to change the course of the future of Panem. To do this, she must put aside her feelings of anger and distrust. She must become the rebels' Mockingjay--no matter what the personal cost.",
             category_name="Trilogy",
             user_id=3)
book12 = Book(id=18,
             title="Bossypants",
             author="Tina Fey",
             description="Bossypants is heartwarming memoir about growth and acceptance by comedian Tina Fey. The memoir recounts Fey’s childhood with clever insight and her trademark humor. Fey shows readers how she first started out in the industry and what lessons she has learned along the way. She also combines the overall narrative of her growth in comedy with seemingly random asides. These asides, or chapters, actually blend in well with the overarching narrative, and add much weight to important topics that Fey deems relevant to the overall concept of empowerment and positivity.

            Fey was born in 1970, in Philadelphia, and lovingly recalls her childhood and her parents, Jeanne and Don. The narrative explains how Fey was introduced to acting at a young age when she began working at a local summer theater camp. Though this event was Fey’s introduction into acting and her future career, this period also highlighted a darker moment in her life, and one that she vehemently speaks out about now. While at the camp, Fey and other girls sabotaged another girl’s acting. The cruel treatment was revenge for the girl “stealing” Fey’s boyfriend of the time. After revealing her involvement in this bullying, Fey then explains just how damaging this type of behavior is for women. She calls this violence on women by women entirely unacceptable. Fey also addresses her anxiety at a young age about finding dates and feeling like she did not belong to a group. This feeling even followed her into her college years, where the popular girls of the time were all blond.",
             category_name="Autobiographies",
             user_id=1)
book13 = Book(id=19,
             title="How Not To Die",
             author="Michael Greger",
             description="The vast majority of premature deaths can be prevented through simple changes in diet and lifestyle. In How Not to Die, Dr. Michael Greger, the internationally-recognized lecturer, physician, and founder of NutritionFacts.org, examines the fifteen top causes of death in America—heart disease, various cancers, diabetes, Parkinson’s, high blood pressure, and more—and explains how nutritional and lifestyle interventions can sometimes trump prescription pills and other pharmaceutical and surgical approaches, freeing us to live healthier lives.

            The simple truth is that most doctors are good at treating acute illnesses but bad at preventing chronic disease. The 15 leading causes of death claim the lives of 1.6 million Americans annually. This doesn’t have to be the case. By following Dr. Greger’s advice, all of it backed up by peer-reviewed scientific evidence, you will learn which foods to eat and which lifestyle changes to make to live longer.

            History of prostate cancer in your family? Put down that glass of milk and add flaxseed to your diet. Have high blood pressure? Hibiscus tea can work better than a leading hypertensive drug—and without the side effects. What about liver disease? Drinking coffee can reduce liver inflammation. Battling breast cancer? Consuming soy is associated with prolonged survival. Worried about heart disease (our #1 killer)? Switch to a whole-food, plant-based diet, which has been repeatedly shown not just to help prevent the disease, but arrest and even reverse it.

            In addition to showing what to eat to help prevent the top 15 causes of death, How Not to Die includes Dr. Greger’s Daily Dozen—a checklist of the foods we should try to consume every day. Full of practical, actionable advice and surprising, cutting edge nutritional science, these doctor’s orders are just what we need to live longer, healthier lives.",
             category_name="Health",
             user_id=4)
book14 = Book(id=20,
             title="The Insanity of God: A True Story of Faith Resurrected",
             author="Nik Ripken & Gregg Lewis",
             description="The Insanity of God is the personal and lifelong journey of an ordinary couple from rural Kentucky who thought they were going on just your ordinary missionary pilgrimage, but discovered it would be anything but. After spending over six hard years doing relief work in Somalia, and experiencing life where it looked like God had turned away completely and He was clueless about the tragedies of life, the couple had a crisis of faith and left Africa asking God, "Does the gospel work anywhere when it is really a hard place?  It sure didn't work in Somalia.
            Nik recalls that, “God had always been so real to me, to Ruth, and to our boys. But was He enough, for the utter weariness of soul I experienced at that time, in that place, under those circumstances?” It is a question that many have asked and one that, if answered, can lead us to a whole new world of faith.",
             category_name="Religion, Spirituality & New Age",
             user_id="")
book15 = Book(id=21,
             title="Afterlife",
             author="Marcus Sakey",
             description="Sakey began his career with a series of smart, compulsively readable thrillers about more or less ordinary Chicagoans wrestling with personal problems and the zeitgeist, and getting into potentially fatal trouble. But with Brilliance (2013) and the Brilliance series that followed, he stepped brilliantly into the realm of speculative fiction. Afterlife is a deep dive into the unknowable. Chicago is being terrorized by a preternaturally lethal sniper, and FBI agents Will Brody and his lover, Claire McCoy, are desperate to end the terror. But Will is murdered by a bomb in an abandoned West Side church. Claire is bereft, but the dead Brody finds himself wandering the streets of a Chicago populated only by people armed with clubs, axes, and swords. Some threaten him, but Will encounters a group of people who lead him to their refuge. Meanwhile, Claire kills the sniper but dies in the effort. The couple are reunited, and they conclude that being together in the afterlife isn’t bad—except for the “eaters,” dead people who have learned that killing makes them stronger. Even worse, the sniper is organizing eaters into an army. Afterlife is simultaneously a beautiful love story, a grim tale of apocalyptic conflict, and an opportunity for an insightful writer to ruminate on the eternal verities. Great appeal across genres.",
             category_name="Horror",
             user_id=4)


session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)
session.add(book7)
session.add(book8)
session.add(book9)
session.add(book10)
session.add(book11)
session.add(book12)
session.add(book13)
session.add(book14)
session.add(book15)
session.commit()
