from instapy import InstaPy  

session = InstaPy(username="Noob._.Developer", password='Qwerty@123')
session.login()

session.set_relationship_bounds(enabled=True,      
                                delimit_by_numbers=True,
				                
								min_following=100,
				                min_followers=100,
								min_posts=10)

session.set_do_comment(enabled=True, percentage=100)
session.set_comments(['Awesome', 
					  'Really Cool',
					  'I like your stuff',
					  'Its Great',
					  'Its, Amazing',
					   'It seems cool'])

session.set_dont_like(['#dog','#cats'])


session.set_user_interact(amount=5, randomize=True, percentage=50,)
session.set_do_follow(enabled=True, percentage=100)
session.set_do_like(enabled=True, percentage=100)

session.interact_user_followers(['natgeo'], amount=10, randomize=True)
session.set_mandatory_words(['#food',
							 '#instafood'])

session.remove_follow_requests(amount=200, sleep_delay=600)

session.set_do_story(enabled = True, percentage = 70, simulate = False)
session.story_by_users(['shirleysetia',
						'earthfever',
						'spacex',
						'foodfuly',
						'barbequenation',
						'planetfervor',
						'nasa'
						])

session.like_by_tags(['#fashion',
					  '#instagood',
					  '#tbt'
					  '#happy'
					  '#vibes'
					  '#travelling'])

				 
session.end()