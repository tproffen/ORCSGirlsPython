# Interactive Plotting helpers

import ipywidgets as widgets
import plotly.graph_objects as go
import numpy as np

from google.colab import output
output.enable_custom_widget_manager()

class PlotSlider():
  def __init__(self, name = 'slider', value = 0, min_value = 0, max_value= 100, step_value = 1):
    self.name = name
    self.value = value
    self.max_value = max_value
    self.min_value = min_value
    self.step_value = step_value

class InteractivePlot():
  def __init__(self, func, sliders=[], xtitle='x',ytitle='y', mode='lines', ymin=None, ymax=None):
    self.func = func
    self.sliders = sliders
    self.xtitle = xtitle
    self.ytitle = ytitle
    self.mode = mode
    self.ymin = ymin
    self.ymax = ymax

    self.graph = None
    self.widget_sliders = []
    self.xvals = []
    self.yvals = []

  def addslider(self,slider):
    self.sliders.append(slider)

  def calc(self):
    args=[p.value for p in self.sliders]
    (self.xvals, self.yvals) = self.func(*args)

  def plot(self):
    if not self.ymin: self.ymin = min(self.yvals)
    if not self.ymax: self.ymax = max(self.yvals)
    
    self.layout = go.Layout(yaxis_range=[self.ymin, self.ymax],
                            xaxis_title=self.xtitle, yaxis_title=self.ytitle,
                            width=800, height=600)
    self.data = go.Scatter(x=self.xvals, y=self.yvals, mode=self.mode, name='Line')
    self.graph = go.FigureWidget(data=[self.data], layout=self.layout)

  def makesliders(self):
    def update(change):
        args=[p.value for p in self.widget_sliders]
        (self.graph.data[0].x, self.graph.data[0].y) = self.func(*args)

    if(len(self.sliders)>0):
      for i in range(len(self.sliders)):
        self.widget_sliders.append(widgets.FloatSlider(
            value=self.sliders[i].value, min=self.sliders[i].min_value,
            max=self.sliders[i].max_value, description=self.sliders[i].name))
        self.widget_sliders[i].observe(update, names='value')

  def show(self):
    self.calc()
    self.plot()
    self.makesliders()
    display(widgets.HBox([self.graph,widgets.VBox(self.widget_sliders)]))
    