from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
class MainScreen(Screen):
    pass

class RuhaniScreen(Screen):
    def update_section_content(self, content):
        self.ids.section_label.text = content

    def back_to_home(self):
        screen_manager = self.manager
        screen_manager.current = 'main'     
       



class MDScreenManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.title = 'KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        screen_manager = MDScreenManager()

        # Add screens to the screen manager
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(RuhaniScreen(name='ruhani'))

        return screen_manager

    
    def show_tailored_for_you(self):
       
        tailored_content = """
**Tailored for You:**
Imagine a workout plan that's as unique as your fingerprints, meticulously designed to cater to your individuality. This approach ensures that every facet of the plan is finely tuned to match your distinct attributes, ensuring an exercise experience that's truly your own.

**Your Body, Your Goals:**
A tailored regimen begins by acknowledging that your body is like no other. Your fitness goals are taken into account to create a plan that's perfectly aligned with what you want to achieve. It's all about making your fitness journey entirely your own.

**Unlocking Your Potential:**
This personalized approach taps into your strengths and potential. It's about identifying what you're naturally good at and capitalizing on those attributes. The result? Workouts that not only feel tailored but also empower you to achieve your best.

**Limitations as Opportunities:**
Everyone has limitations, but a personalized plan turns those limitations into opportunities. Whether you're dealing with past injuries or specific preferences, the plan adapts to ensure that you're always pushing boundaries in a safe and effective way.

**Progress on Your Terms:**
Progression is essential, but not at the cost of comfort. A tailored plan allows for gradual progress, ensuring that you're always challenging yourself while feeling confident and capable in every step you take.

**A Journey You Enjoy:**
Ever had a workout that felt like a chore? A personalized plan turns that around. By incorporating activities you genuinely enjoy, it transforms your fitness journey into something exciting, encouraging consistency and a positive mindset.

**Results Crafted for You:**
At the core of personalization is a focus on results that truly matter to you. Instead of a one-size-fits-all approach, the plan zeroes in on exercises that align with your objectives, making every sweat session purposeful and rewarding.

"""

        self.root.get_screen('ruhani').update_section_content(tailored_content)
        self.root.current = 'ruhani' 
        
    def show_evolving_with_you(self):
        evolving_content = """
**Evolving with You: A Fitness Journey of Transformation**

Embarking on a fitness journey is akin to embarking on a quest of personal evolution. Just as the seasons change, so does our body's capacity to adapt, grow, and transform. In the realm of fitness, the concept of "evolving with you" takes center stage – it's the acknowledgment that your journey is dynamic, and so is the approach to achieving your health and fitness goals.

At its core, "evolving with you" encapsulates the idea that fitness is not a one-size-fits-all endeavor. It's not about adhering to a rigid routine or following a cookie-cutter plan; rather, it's a deeply personalized experience that molds itself to your unique needs, desires, and circumstances. Just as a chameleon adapts to its surroundings, your fitness routine should adapt to your changing goals, preferences, and limitations.

As you progress on your journey, your body transforms, and so do your aspirations. What once seemed like a monumental achievement becomes a stepping stone to greater heights. It's not just about pushing the boundaries; it's about redefining them. "Evolving with you" is the compass that guides you through this transformation, ensuring that your path aligns with your evolving goals.

Flexibility is the cornerstone of this approach. Life is a tapestry woven with various threads – work commitments, family responsibilities, and personal aspirations. A successful fitness journey acknowledges these threads and finds ways to weave exercise seamlessly into the fabric of your life. Whether it's adjusting your workout schedule or finding innovative ways to stay active, "evolving with you" is about staying agile in the face of change.

But it's not just about the physical aspect. Mental and emotional growth are integral components of your fitness evolution. Self-awareness, self-compassion, and a positive mindset all play a pivotal role in your journey's trajectory. "Evolving with you" encourages mindfulness, helping you tap into your inner strengths and conquer the hurdles that stand in your way.

And just as a caterpillar undergoes metamorphosis to become a butterfly, your journey is marked by transformative moments. Milestones become symbols of triumph, obstacles become stepping stones, and setbacks become opportunities for growth. "Evolving with you" is about embracing the entirety of your journey – the highs, the lows, and the beautiful transformations that unfold along the way.

In a world that's constantly changing, "evolving with you" is the anthem of adaptability, growth, and empowerment. It's a reminder that your fitness journey is a lifelong voyage, one that reflects the beautiful tapestry of your evolving self. So lace up your sneakers, set your intentions, and let "evolving with you" guide you to new horizons, one step at a time.
"""
        self.root.get_screen('ruhani').update_section_content(evolving_content)

        self.root.current = 'ruhani' 

    def show_smart_exercise_choices(self):
        smart_exercise_content = """
**Smart Exercise Choices: A Guide to Effective Workouts**

In the realm of fitness, making smart exercise choices is paramount to achieving your health and wellness goals. Gone are the days of mindlessly going through the motions – today, it's all about adopting a strategic approach that maximizes results while minimizing the risk of injury. From cardio enthusiasts to weightlifting aficionados, everyone can benefit from understanding the significance of intelligent exercise selection.

**Understanding Smart Exercise Choices**

Smart exercise choices go beyond simply picking exercises at random. It involves a holistic understanding of your body, fitness objectives, and the principles of exercise science. Here's a breakdown of what it entails:

**1. Goal Alignment:**
Begin by defining your fitness goals. Are you aiming for muscle gain, weight loss, cardiovascular fitness, or overall functional strength? Each goal requires a different exercise approach. For instance, a muscle-building regimen would focus on resistance training, while weight loss might involve a mix of cardio and high-intensity interval training (HIIT).

**2. Target Muscle Groups:**
Identify the muscle groups you want to target. A well-rounded workout routine should include exercises that engage various muscle groups, ensuring balanced development and reducing the risk of muscle imbalances.

**3. Exercise Variation:**
Variety is the spice of life, and it holds true in fitness. Incorporate a mix of compound and isolation exercises to target different muscle fibers and movement patterns. Compound exercises, such as squats and deadlifts, engage multiple muscle groups simultaneously, while isolation exercises, like bicep curls, focus on specific muscles.

**4. Functional Movements:**
Consider exercises that mimic everyday movements. Functional exercises not only enhance strength and stability but also improve your ability to perform daily tasks with ease.

**5. Rest and Recovery:**
Don't underestimate the importance of rest and recovery. Alternating between muscle groups and incorporating rest days prevents overtraining and allows your muscles to repair and grow.

**Creating a Smart Workout Plan**

Now, let's put theory into practice with a sample smart workout plan. Remember, this plan is a general guideline; tailor it according to your fitness level, preferences, and any existing medical conditions.

[... Workout Plan ...]

**Conclusion: Making Every Rep Count**

The essence of smart exercise choices lies in making every rep count. By aligning your exercises with your goals, targeting specific muscle groups, and embracing variety, you set the stage for a transformative fitness journey. Remember, consistency is key, and always listen to your body. As you progress, feel free to adjust your workout plan to challenge yourself and continue making steady progress.

Whether you're a seasoned athlete or just beginning your fitness journey, embracing smart exercise choices ensures that your efforts translate into tangible results. So, lace up your sneakers, hydrate, and get ready to embark on a fitness adventure that's backed by science, strategy, and the power of intelligent movement. Your body will thank you for it!
"""
        self.root.get_screen('ruhani').update_section_content(smart_exercise_content)

        self.root.current = 'ruhani' 

    def show_real_time_guidance(self):
        real_time_guidance_content = """
**Real-Time Guidance: Elevating Your Fitness Experience**

In a world driven by technology, it's only natural that the realm of fitness has embraced the power of real-time guidance. No longer confined to static routines, fitness enthusiasts now have the luxury of real-time feedback, tracking, and motivation. Welcome to the era of real-time guidance – where your workout becomes an interactive and dynamic experience.

**The Era of Interaction**

Real-time guidance isn't just about having a fitness app count your steps; it's about personalized interactions that elevate your workout to new heights. Imagine having a virtual trainer by your side, analyzing your form, providing instant feedback, and adjusting your workout in real-time to optimize results.

**1. Form and Technique:**
One of the most significant benefits of real-time guidance is its ability to assess your form and technique. Whether you're lifting weights, doing yoga, or performing bodyweight exercises, the technology can detect subtle errors and provide cues to ensure you're executing each movement correctly. This minimizes the risk of injury and maximizes the effectiveness of your workout.

**2. Customized Workouts:**
Real-time guidance tailors your workouts to your fitness level and goals. Based on your performance and progress, the system can adjust the intensity, volume, and exercises to ensure you're always challenged but not overwhelmed. This adaptability keeps your workouts engaging and effective.

**3. Feedback Loop:**
Prompt feedback is a game-changer. Instead of waiting until the end of your session to review your progress, real-time guidance gives you insights as you go. Whether it's tracking your heart rate, calories burned, or the number of reps completed, you're always in the loop, making data-driven decisions.

**4. Motivation and Accountability:**
Staying motivated can be a challenge, especially when working out alone. Real-time guidance adds a layer of accountability by providing positive reinforcement, rewards for achieving milestones, and reminders to stay on track. It's like having a virtual workout buddy cheering you on.

**5. Flexibility and Convenience:**
Life is unpredictable, and your fitness routine should be flexible enough to accommodate changes. Real-time guidance offers on-the-fly adjustments, allowing you to customize your workout duration, exercises, and intensity based on your schedule and energy levels.

**Looking Ahead: The Future of Fitness**

As technology continues to evolve, so does the potential of real-time guidance. Imagine augmented reality glasses guiding you through workouts, virtual trainers assessing your biomechanics, and AI algorithms predicting your performance trends. The future of fitness is an immersive, data-rich experience that empowers you to achieve your goals like never before.

**Conclusion: Your Personal Fitness Companion**

Real-time guidance transforms your fitness routine into an interactive and dynamic adventure. It bridges the gap between traditional workouts and cutting-edge technology, enhancing your form, motivation, and overall fitness journey. So, whether you're a tech enthusiast or simply looking to maximize your workout efficiency, real-time guidance is your personal fitness companion, guiding you towards a healthier, stronger, and more empowered you.
"""
        self.root.get_screen('ruhani').update_section_content(real_time_guidance_content)
        self.root.current = 'ruhani' 

    def show_tracking_your_success(self):
        tracking_success_content = """
**Tracking Your Success: The Power of Progress Monitoring**

Embarking on a fitness journey is much like embarking on a quest for personal transformation. One of the most valuable tools in your arsenal is the ability to track your progress – to tangibly see how far you've come, celebrate milestones, and stay motivated as you work towards your fitness goals. Tracking your success isn't just about data; it's about understanding and embracing the journey.

**1. Setting Clear Objectives:**
Effective progress tracking begins with setting clear and achievable objectives. Whether you're aiming to increase your strength, improve your cardiovascular endurance, or shed a few pounds, defining specific goals gives you a target to work towards. These objectives become the foundation for the metrics you'll track.

**2. Quantifiable Metrics:**
The beauty of progress tracking lies in its quantifiable nature. Metrics such as weight, body measurements, reps completed, distances covered, and even mood indicators provide you with tangible evidence of your progress. These metrics enable you to objectively assess your journey.

**3. Celebrating Milestones:**
Every journey is dotted with milestones, both big and small. Progress tracking allows you to celebrate these achievements, reinforcing a sense of accomplishment. Whether it's hitting a new personal record or consistently following your routine, acknowledging your victories fuels your motivation to continue.

**4. Identifying Patterns:**
Tracking your progress over time unveils patterns and trends that might otherwise go unnoticed. You can identify which strategies are yielding the best results, understand how your body responds to different approaches, and make informed decisions about adjusting your routine.

**5. Staying Accountable:**
When you're accountable to yourself and your goals, you're more likely to stay committed. Progress tracking creates a sense of responsibility. Knowing that you're monitoring your journey can prevent you from skipping workouts or neglecting your nutrition plan.

**6. Staying Motivated:**
The sight of progress can be a powerful motivator. Visualizing how far you've come, whether through progress photos or tracking charts, encourages you to keep pushing forward. Even during plateaus, seeing the journey you've traveled can reignite your motivation.

**7. The Journey, Not Just the Destination:**
It's important to note that tracking your success isn't just about the destination; it's about embracing the entire journey. There will be ups and downs, challenges and triumphs. Progress tracking helps you see the growth, resilience, and dedication that shape your story.

**8. Harnessing Technology:**
In the digital age, progress tracking has been made easier with the help of fitness apps, wearable devices, and online platforms. These tools streamline data collection, visualization, and analysis, making it simpler than ever to monitor your success.

**Conclusion: Your Personal Fitness Diary**

Tracking your success is like keeping a personal fitness diary – a chronicle of your growth, efforts, and accomplishments. It's a tool that empowers you to stay focused, make informed decisions, and appreciate the transformative journey you're on. So, whether you're aiming for better health, increased strength, or enhanced performance, embrace the power of progress tracking and embark on a journey that's as rewarding as the destination.
"""
        self.root.get_screen('ruhani').update_section_content(tracking_success_content)

        self.root.current = 'ruhani' 

    def show_recovery_and_prevention(self):
        recovery_prevention_content = """
**Recovery and Prevention: Nurturing Your Body's Resilience**

In the pursuit of fitness, it's easy to focus solely on the sweat-drenched workouts and intense training sessions. However, the magic of progress happens not just during the grind, but during recovery. Recovery and prevention are the unsung heroes that allow your body to bounce back, grow stronger, and ward off potential injuries. It's the art of giving your body the care it deserves.

**1. The Science of Recovery:**
Recovery is the process by which your body repairs itself after exertion. It involves replenishing energy stores, repairing damaged tissues, and optimizing hormonal balance. Neglecting recovery can lead to burnout, decreased performance, and increased risk of injuries.

**2. Prioritizing Sleep:**
Sleep isn't just a luxury; it's a necessity for recovery. During sleep, your body releases growth hormones, repairs damaged cells, and restores energy levels. Prioritize a consistent sleep schedule and aim for 7-9 hours of quality sleep each night.

**3. Active Recovery:**
Active recovery involves engaging in low-intensity activities that stimulate blood flow and promote healing without putting strain on your body. Activities like gentle yoga, light swimming, or leisurely walks can aid in reducing muscle soreness and enhancing overall recovery.

**4. Proper Nutrition:**
Nutrition plays a crucial role in recovery. Consuming a balanced diet rich in protein, healthy fats, vitamins, and minerals provides the building blocks your body needs for repair and growth. Post-workout meals and hydration are especially important to refuel and replenish.

**5. Hydration and Electrolyte Balance:**
Staying hydrated is essential for recovery. Water helps transport nutrients, remove waste products, and regulate body temperature. Additionally, maintaining electrolyte balance through foods or electrolyte supplements aids in muscle function and overall recovery.

**6. Listen to Your Body:**
Your body is an excellent communicator. Pay attention to signs of fatigue, soreness, and pain. Overtraining and ignoring these signals can lead to injury. Allow your body adequate time to heal and adjust your training accordingly.

**7. Incorporating Rest Days:**
Rest days are not a sign of weakness; they're a strategic component of a successful fitness journey. Rest allows your body to recharge and adapt to the stress of exercise. Design your training plan to include regular rest days.

**8. Injury Prevention:**
Prevention is the first line of defense against injuries. Incorporate dynamic warm-ups, proper technique, and gradual progression into your routine. Also, include exercises that strengthen stabilizing muscles and address muscle imbalances.

**9. Mobility and Flexibility:**
Maintaining good flexibility and mobility is crucial for preventing injuries. Incorporate dynamic stretching and mobility exercises into your routine to improve joint range of motion and reduce the risk of strains.

**10. Mental Recovery:**
Recovery isn't just physical; it's mental too. High levels of stress and mental fatigue can hinder recovery. Practice relaxation techniques, mindfulness, and stress management to support your overall well-being.

**Conclusion: Nurturing Wellness Through Recovery**

Recovery and prevention are integral parts of your fitness journey, fostering a cycle of growth, resilience, and lasting health. Prioritize your body's need for restoration, both physically and mentally. By embracing the art of recovery and incorporating preventive measures, you're not just nurturing your body; you're laying the foundation for a sustainable, fulfilling, and injury-free fitness lifestyle.
"""
        self.root.get_screen('ruhani').update_section_content(recovery_prevention_content)

        self.root.current = 'ruhani' 

if __name__ == "__main__":
    MainApp().run()
