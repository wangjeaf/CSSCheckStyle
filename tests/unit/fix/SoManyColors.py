from helper import *

def doTest():
    css = '''.ui-dialog .ui-dialog-content .btn.confirm {
  background-color: #2996e3;
  background-image: -moz-linear-gradient(top, #2692de, #2d9deb);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#2692de), to(#2d9deb));
  background-image: -webkit-linear-gradient(top, #2692de, #2d9deb);
  background-image: -o-linear-gradient(top, #2692de, #2d9deb);
  background-image: linear-gradient(to bottom, #2692de, #2d9deb);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff2692', endColorstr='#ff2d9d', GradientType=0);
  color: #ffffff;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75);
  border-color: #2D9DEB;
}'''

    expected = '''.ui-dialog .ui-dialog-content .btn.confirm {
    border-color: #2D9DEB;
    background-color: #2996E3;
    background-image: -moz-linear-gradient(top,#2692DE,#2D9DEB);
    background-image: -webkit-gradient(linear,0 0,0 100%,from(#2692DE),to(#2D9DEB));
    background-image: -webkit-linear-gradient(top,#2692DE,#2D9DEB);
    background-image: -o-linear-gradient(top,#2692DE,#2D9DEB);
    background-image: linear-gradient(to bottom,#2692DE,#2D9DEB);
    background-repeat: repeat-x;
    color: #FFF;
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#FF2692',endColorstr='#FF2D9D',GradientType=0);
    text-shadow: 0 1px 1px rgba(255,255,255,.75);
}'''
    fixer, msg = doFix(css, '')
    equal(msg, expected, 'so many colors are ok');
