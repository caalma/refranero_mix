import random, strformat, strutils, linenoise

randomize()

proc separar(tex, modo: string): seq[string] =
    var
      s = ""
      agregar = true

    result = @["", ""]

    case modo:
    of  "una_coma":
      s = ","
    of "un_puntoycoma":
      s = ";"
    of "separacion_manual":
      s = "|"
      agregar = false
    else: discard
    result = tex.split(s)
    if agregar:
        result[0] &= s

const
  nl = "\n"
  bd_disponibles = @[
    ["una_coma", "./bd/con_una_coma.txt"],
    ["un_puntoycoma", "./bd/con_un_punto_y_coma.txt"],
    ["separacion_manual", "./bd/con_separacion_manual.txt"]
  ]

let
  mi = rand(0..(bd_disponibles.len - 1))
  modo = bd_disponibles[mi][0]
  bd = bd_disponibles[mi][1].readFile.split("\n")
  ri1 = rand(0..(bd.len - 1))

var ri2 = rand(0..(bd.len - 1))

while ri2 == ri1:
    ri2 = rand(0..(bd.len - 1))

var
  r1 = bd[ri1]
  r2 = bd[ri2]
  rp1 = r1.separar(modo)[0]
  rp2 = r2.separar(modo)[1]

if modo == "separacion_manual":
    r1 = r1.replace("|", "")
    r2 = r2.replace("|", "")

clearScreen()
echo fmt"{nl}==  {rp1}{rp2}  =={nl}"
echo fmt":1  {r1}"
echo fmt":2  {r2}"
