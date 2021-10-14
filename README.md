# Geometrical quantities from metric tensor

The geometrical properties of a curved space can be derived from the metric tensor, which is encoded in the line element 

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0Ads%5E2+%3D+g_%7B%5Cmu+%5Cnu%7D+dx%5E%5Cmu+dx%5E%5Cnu%0A">

From <img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0A+g_%7B%5Cmu+%5Cnu%7D+%0A"> we can compute geometrical quantities such as 

- Christoffel symbol

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0A%5CGamma%5E%7B%5Calpha%7D_%7B%5Cbeta+%5Cgamma%7D+%3D+%5Cfrac%7B1%7D%7B2%7D+g%5E%7B%5Calpha+%5Cdelta%7D+%5Cleft%28+%5Cpartial_%5Cbeta+g_%7B%5Cdelta+%5Cgamma%7D+%2B+%5Cpartial_%5Cgamma+g_%7B%5Cdelta+%5Cbeta%7D+-+%5Cpartial_%5Cdelta+g_%7B%5Cbeta+%5Cgamma%7D+%5Cright%29">

- Riemann tensor

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0AR%5E%5Cdelta_%7B%5Calpha+%5Cbeta+%5Cgamma%7D+%3D+%5Cpartial_%5Cbeta+%5CGamma_%7B%5Calpha+%5Cgamma%7D%5E%7B%5Cdelta%7D+-+%5Cpartial_%5Cgamma+%5CGamma_%7B%5Calpha+%5Cbeta%7D%5E%7B%5Cdelta%7D+%2B+%5CGamma_%7B%5Calpha+%5Cgamma%7D%5E%7B%5Cepsilon%7D+%5CGamma_%7B%5Cepsilon+%5Cbeta%7D%5E%7B%5Cdelta%7D+-+%5CGamma_%7B%5Calpha+%5Cbeta%7D%5E%7B%5Cepsilon%7D+%5CGamma_%7B%5Cepsilon+%5Cgamma%7D%5E%7B%5Cdelta%7D">

- Ricci tensor

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0AR_%7B%5Calpha%5Cbeta%7D+%3D+R%5E%5Clambda_%7B%5Calpha+%5Clambda+%5Cbeta%7D">

- Ricci scalar 

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0AR+%3D+g%5E%7B%5Calpha+%5Cbeta%7D+R_%7B%5Calpha+%5Cbeta%7D">

- Einstein tensor 

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ccolor%7Bgrey%7D%0AG_%7B%5Calpha+%5Cbeta%7D+%3D+R_%7B%5Calpha+%5Cbeta%7D+-+%5Cfrac%7B1%7D%7B2%7D+g_%7B%5Calpha+%5Cbeta%7D+R">


These quantities are found symbolically with Induced_geometry.py It was tested with two metrics, the one of an embedded 3-Sphere and the FLRW metric. 
