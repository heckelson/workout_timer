# timer.py
import yaml
import time

class WorkoutTimer:
    def __init__(self):
        with open("workout_timer.yaml") as f:
            params = yaml.load(f, Loader=yaml.FullLoader)
            self.reps = int(params['reps'])
            self.exercises = params['exercises']
            self.exercise_duration = params['exercise_duration']
            self.break_duration = params['break_duration']
            self.long_break_duration = params['long_break_duration']
            self.long_break_after = params['long_break_after']
                
            print("Your workout parameters:")
            print(f"  Reps: {self.reps}")
            print(f"  Exercises: {self.exercises}")
            print(f"  Exercise duration: {self.exercise_duration}s")
            print(f"  Break duration: {self.break_duration}s")
            print(f"  Long Break duration: {self.long_break_duration}s")
            print(f"  Long breaks after: {self.long_break_after} reps")

            total_duration = (self.reps * (self.exercises * (self.exercise_duration + self.break_duration)) + (self.reps // self.long_break_after) * self.long_break_duration) / 60

            print(f"  Total duration of the workout: about {total_duration} minutes")


            for i in range(self.reps):
                print(f"Rep {i}")
                for j in range(self.exercises):
                    print(f"  Exercise {j}")
                    print(f"    Exercise for {self.exercise_duration} seconds")
                    time.sleep(self.exercise_duration)
                    print(f"    Take a break for {self.break_duration} seconds")
                    time.sleep(self.break_duration)
                if (i+1) % self.long_break_after == 0:
                    print(f"    Take a long break for {self.long_break_duration} seconds")
                    time.sleep(self.long_break_duration)

if __name__ == "__main__":
    workout_timer = WorkoutTimer()
    
