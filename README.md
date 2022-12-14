# Numerical-methods
Examples of numerical methods to solve ordinary equations and partial differential equations with python

## Example
* **Runge–Kutta methods**

A Runge-Kutta method with s-stages and order p is a method in the form

<img
  src="https://latex.codecogs.com/svg.image?x_{n&plus;1}=&space;x_{n}&space;&plus;&space;\sum&space;_{i=1}^{s}&space;b_{i}.&space;k_{i}" title="x_{n&plus;1}=&space;x_{n}&space;&plus;&space;\sum&space;_{i=1}^{s}&space;b_{i}.&space;k_{i}"
/>

with 

<img
  src="https://latex.codecogs.com/svg.image?k_{i}&space;=&space;f(x_{n}&space;&plus;&space;\sum_{j=1}^{s}&space;a_{ij}.k_{j}&space;,&space;t_{n}&space;&plus;&space;h&space;c_{i})" title=""
/>

and the error holds the condition 

<img
  src="https://latex.codecogs.com/svg.image?Max&space;\left|&space;x(t_{i})&space;-&space;x_{i}&space;\right|&space;=&space;Ch&space;t^{p}" title=""
/>
* **Picard's iterative method**

Picard's method is mostly used in mathematical studies of differential equations.

* **Discretization methods to solve Heat equation**

The heat equation can be written in general terms:

<img
  src="https://latex.codecogs.com/svg.image?\frac{\partial&space;T}{\partial&space;t}&space;=&space;\alpha&space;\frac{\partial^2&space;T}{\partial&space;x^2}" title=""
/>

where

<img
  src="https://latex.codecogs.com/svg.image?\alpha&space;=&space;\frac{\lambda&space;}{\mu&space;C}&space;" title=""
/>

is the thermal diffusivity.


## 🚀 Author
Jaurès Ratsimbazafiharivola **[Matrix Tera]**

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
