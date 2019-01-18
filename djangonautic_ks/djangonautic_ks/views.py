from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from mainpage.models import user_list



sentence = ['The rain was falling heavily.',' It was like driving through a thick curtain of water.',
'He eased off the accelerator a little.','Had to be careful driving on wild nights like these.',
' The las thing you’d want is to have an accident or breakdown.', 'You just want to be at home on these stormy nights.',
' The thwack-thwack of the windscreen wipers was hypnotic.', 'He stared out into the glow of the headlights.', 
'The rain sounded like white noise interference as it battered the car.','He was reminded of the opening scenes of a Hitchcock film.', 
'Through the wash of the rain he spotted a figure at the side of the road.', 'The person wore a green parka and had their thumb jerked out.', 
'Why on earth would anyone be hitchhiking tonight?', 'Surely you would just stay put until the morning.',
 'They must have been in a rush to get where they were going.', 'He signalled down and pulled over.', 
 'The hitchhiker climbed in.', 'He shut the door quickly, glad to be out of the rain.', 'He pulled his hood back and sighed.', 
 'He was somewhere in his mid-twenties and had wild red hair and a thick beard.', 'Awful night, eh? said the driver.', 
 'The hitchhiker held his gaze for a long moment.','Drops of rainwater trickled down his face.', 'Yes. Yes it is.', 
 'The driver pulled out and continued through the storm.', 'The hitcher glanced over his shoulder into the blackness behind them.',
 'You okay?', 'The hitcher simply nodded.','They drove on in silence for a short while.',
 'The BBC radio phone in blaring out from the car’s speakers filled in for conversation.', 
 'They listened to the radio and their own thoughts as they moved on.', 'Where are you headed? asked the driver',
 'North. The hitcher pointed.','Are you travelling to visit friends?Hmph...','The driver couldn’t tell if that was a yes or a no.',
 ' He adjusted his tie nervously.',' The hitcher stared at him in his suit and tie.',
 'The hitcher seemed scruffy in comparison in his parka and Pink Floyd t-shirt.','Do you work around here?’ asked the hitcher.',
 'Yes. said the driver.','I was stuck late at the office.', ' You know how it is. No. Not really', 'Again they drifted into silence.',
 'The talk radio show carried on as they drove through the wind and rain.''The hitcher shifted in his seat and stared out the windscreen.',
 'No music?’ the hitcher asked. What?', 'Is there no music we could listen to?','I like the talk radio shows. I’m not really a music fan.',
 'The hitcher’s eyes glazed over for a moment. Then he spoke.','I like listening to music. It calms me down.','The driver said nothing.',
 'Several miles later there was a news bulletin on the radio.','The reporter tried to remain professional as she read the announcement.',
 'We are getting reports that a patient has escaped from a Manchester psychiatric institution.',
 'The man is said to be psychopathic and is said to have a history of murder.', 'The hitcher jabbed a finger on the button on the radio panel.',
 'Tinny pop music blurted out from the speakers.','The driver stared at his passenger, his question unasked.',
 'I hate the news. answered the hitcher.',' It’s so depressing. It brings me down.', 'There is never any good news, is there?',
 'The driver did not reply.','Don’t worry. I’m not the killer, said the hitcher, fidgeting with his coat.', 
 'No? said the driver. I mean, no, of course you aren’t.','They drove on listening to the crappy pop music and over-excited radio DJs.',
 ' The rain pounded on the car.','What do you do for a living?’ asked the driver.','The hitcher was quiet for a moment. Then he grinned.',
 'I’m a writer.','Really? How interesting. Have you had anything published?','No. As yet I’m an undiscovered artist.',
 'I’m sure you will make it.',' What are you working on at the moment?','I’m writing a novel.Yes?It’s about a serial killer.', 
 'The driver did not speak. ','He flicked the talk radio station back on.',
 'A man was rambling on with himself about the change in days his wheelie bins were emptied.',
 'The hitcher said nothing.',' When the driver glanced round his passenger had his eyes closed.',' He was either asleep or feigning slumber.',
 'Where can I drop you?’ asked the driver.','They drove on through the storm down the snaking lanes.', 
 'An hour later. The storm still growled and raged.',' The hitcher looked out of the window, the driver steered the car, in silence.', 
 'Another news bulletin came over the radio.','We’re getting more information on the escaped patient. ','The killer’s name is Simon Hughes.',
 'He escaped from the Green Pastures institute earlier this evening.','He is extremely dangerous and completely unpredictable.',
 'Simon Hughes made his escape by changing from his hospital issue',' uniform into a suit and tie and pretending to be one of the medical staff.',
 'He stole a car and drove off.','The hitcher turned to the driver','What did you say your name was? My name is Simon.',
 'The hitcher stared in shock. Simon grinned.',' The headlights of a passing car glinted off the knife blade in Simon’s hand.']
index=0

def homepage(request):
	return render(request,'homepage.html')

def signup_view(request):
	global index

	if request.method == 'POST':
		
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log the user in
			login(request, user)
			print("in Signup post")
			name=user_list.objects.create(user_name=str(user), index=0)
			name.save()

			
			return redirect('mainpage:mainpage')
	else:
		form = UserCreationForm()
	return render(request, 'Signup.html',{'form':form})

def login_view(request):
	global index

	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			
			name=user_list.objects.get(user_name=str(user))
			index=name.index

			return redirect('mainpage:mainpage')

			
	else:
		form = AuthenticationForm()
	return render(request,'Login.html',{'form':form})


def logout_view(request):
	if request.method=='POST':
		logout(request)
		return render(request, 'homepage.html')

def thankyou_view(request):
	return render(request,'thankyou.html')


