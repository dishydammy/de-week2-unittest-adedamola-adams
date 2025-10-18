class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""

    GLUCOSE_PER_CARB = 0.3      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.5  # fixed decrease per minute of exercise


    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
      self.glucose_level = glucose_level
      self.insulin_sensitivity = insulin_sensitivity
      self.target_glucose = target_glucose
      self.tolerance = tolerance

    def meal(self, carbs: float):
      """Simulate a meal event (input feature: carbs)."""
      self.glucose_level += carbs * self.GLUCOSE_PER_CARB

    def exercise(self, duration: float):
      """Simulate physical activity (input feature: duration in minutes)."""
      self.glucose_level -= duration * self.GLUCOSE_BURN_PER_MIN
    
    def deliver_insulin(self, dose: float):
      """Delivers the right dose of Insulin needed to bring glucose to the appropiate level."""
      if self.insulin_sensitivity <= 0 or self.GLUCOSE_PER_CARB <=0:
        raise ValueError('Sensitivity and Glucose_per_carb must be greater than 0')
     
      if self.glucose_level > self.target_glucose + self.tolerance:
        self.glucose_level -= dose * self.insulin_sensitivity
      else:
        return "Glucose level is okay, no need for insulin"

    def recommend_action(self, auto_apply=False):
      """
      Predict and apply an appropriate system action.
      Acts like a decision function in a model.
      """
      if self.insulin_sensitivity <= 0 or self.GLUCOSE_PER_CARB <=0:
        raise ValueError('Sensitivity and Glucose_per_carb must be greater than 0')
      if self.glucose_level > self.target_glucose + self.tolerance:
        dose = (self.glucose_level - self.target_glucose)/self.insulin_sensitivity
        glucose_level_message = f"Glucose level is too high at {self.glucose_level}"
        action = f"Deliver insulin with this amount: {round(dose,2)}"
        
        if auto_apply:
          self.deliver_insulin(dose)
        return glucose_level_message, action

        
      elif self.glucose_level < self.target_glucose - self.tolerance:
        carbs = (self.target_glucose - self.glucose_level)/self.GLUCOSE_PER_CARB
        glucose_level_message = f"Glucose level is too low at {self.glucose_level}"
        action = f"Eat carbs with a minimum amount of {round(carbs,2)}"
        
        if auto_apply:
          self.meal(carbs)
        return glucose_level_message, action
      
      else:
        glucose_level_message = f"Glucose level is okay at {self.glucose_level}"
        action = "Maintain level"
        return glucose_level_message, action