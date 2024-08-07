INSTRUCTION = """
1. Start from section which starts to cover material requirments
2. Search for core material
3. Omit options which does not contain picked core material
4. Search for fronts thikness 
5. Omit options which does not contain picked core material and defined  fronts thikness 
6. Search for fronts and ends materials. 
6.a If fronts and ends materials are not specified or are not matched with TFL, HPL, or A-Tech Surface, pick HPL as default option.
"""

OPTIONS = """
{
  "options": [
    {
      "series": "1100-C - Sq Flat Edge HPL Frts & HPL Ends IPB CARB Compliant Core",
      "fronts": "Square Flat Edge High Pressure Laminate",
      "ends": "High Pressure Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "1100-N - Sq Flat Edge HPL Frts & HPL Ends NAUF PB Core",
      "fronts": "Square Flat Edge High Pressure Laminate",
      "ends": "High Pressure Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "1150-C - Sq Flat Edge HPL Frts & TF Ends IPB CARB Compliant Core",
      "fronts": "Square Flat Edge High Pressure Laminate",
      "ends": "Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "1150-N - Sq Flat Edge HPL Frts & TF Ends NAUF PB Core",
      "fronts": "Square Flat Edge High Pressure Laminate",
      "ends": "Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "1200-C - 3mm HPL Frts & HPL Ends IPB CARB Compliant Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "High Pressure Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "High Pressure Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "1250-C - 3mm HPL Frts & TF Ends IPB CARB Compliant Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "1250-N - 3mm HPL Frts & TF Ends NAUF PB Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "1600-C - Wood Veneer Frts 3mm Wood Edge & HPL Ends IPB CARB Compliant Core",
      "fronts": "Wood Veneer with 3mm Wood Edge",
      "ends": "High Pressure Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "1600-N - Wood Veneer Frts 3mm Wood Edge & HPL Ends NAUF PB Core",
      "fronts": "Wood Veneer with 3mm Wood Edge",
      "ends": "High Pressure Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "2100-C - Sq Flat Edge TF Frts & Ends IPB CARB Compliant Core",
      "fronts": "Square Flat Edge Thermally Fused Laminate",
      "ends": "Square Flat Edge Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "2100-N - Sq Flat Edge TF Frts & Ends NAUF PB Core",
      "fronts": "Square Flat Edge Thermally Fused Laminate",
      "ends": "Square Flat Edge Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "2200-C - 3mm TF Frts & Ends IPB CARB Compliant Core",
      "fronts": "3mm Thermally Fused Laminate",
      "ends": "3mm Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "2200-N - 3mm TF Frts & Ends NAUF PB Core",
      "fronts": "3mm Thermally Fused Laminate",
      "ends": "3mm Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "2600-C - Wood Veneer Frts 3mm Wood Edge & TF Color Throughout IPB CARB Compliant Core",
      "fronts": "Wood Veneer with 3mm Wood Edge",
      "throughout": "Thermally Fused Laminate Color",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "2600-N - Wood Veneer Frts 3mm Wood Edge & TF Color Throughout NAUF PB Core",
      "fronts": "Wood Veneer with 3mm Wood Edge",
      "throughout": "Thermally Fused Laminate Color",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "2700-C - Sq Flat Edge Frts & TF Color Throughout IPB CARB Compliant Core",
      "fronts": "Square Flat Edge",
      "throughout": "Thermally Fused Laminate Color",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "2700-N - Sq Flat Edge Frts & TF Color Throughout NAUF PB Core",
      "fronts": "Square Flat Edge",
      "throughout": "Thermally Fused Laminate Color",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "2800-C - 3mm Frts & TF Color Throughout IPB CARB Compliant Core",
      "fronts": "3mm",
      "throughout": "Thermally Fused Laminate Color",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "2800-N - 3mm Frts & TF Color Throughout NAUF PB Core",
      "fronts": "3mm",
      "throughout": "Thermally Fused Laminate Color",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "3100 - Sq Flat Edge HPL Frts & Ends Plywood Core Cabinet Box",
      "fronts": "Square Flat Edge High Pressure Laminate",
      "ends": "Square Flat Edge High Pressure Laminate",
      "core": "Plywood Cabinet Box"
    },
    {
      "series": "3200 - 3mm HPL Frts & Ends Plywood Core Cabinet Box",
      "fronts": "3mm High Pressure Laminate",
      "ends": "3mm High Pressure Laminate",
      "core": "Plywood Cabinet Box"
    },
    {
      "series": "3600 - Wood Veneer Frts 3mm Wood Edge & HPL Ends Plywood Core Cabinet Box",
      "fronts": "Wood Veneer with 3mm Wood Edge",
      "ends": "High Pressure Laminate",
      "core": "Plywood Cabinet Box"
    },
    {
      "series": "4200-C - 3mm Frts & A-Tech Surface Throughout IPB CARB Compliant Core",
      "fronts": "3mm",
      "throughout": "A-Tech Surface",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "4200-N - 3mm Frts & A-Tech Surface Throughout NAUF PB Core",
      "fronts": "3mm",
      "throughout": "A-Tech Surface",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "4400-C - 3mm Frts & A-Tech Surface Throughout IPB CARB Compliant Core",
      "fronts": "3mm",
      "throughout": "A-Tech Surface",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "4400-N - 3mm Frts & A-Tech Surface Throughout NAUF PB Core",
      "fronts": "3mm",
      "throughout": "A-Tech Surface",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "4700 - 3mm Wood Edge and Wood Veneer Frts & Ends",
      "fronts": "3mm Wood Edge and Wood Veneer",
      "ends": "3mm Wood Edge and Wood Veneer",
      "core": "Not Specified"
    },
    {
      "series": "5120-C - 3mm HPL Frts & Ends IPB CARB Compliant Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "3mm High Pressure Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "5120-N - 3mm HPL Frts & Ends NAUF PB Core",
      "fronts": "3mm High Pressure Laminate",
      "ends": "3mm High Pressure Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "5220-C - 3mm TF Frts & Ends IPB CARB Compliant Core",
      "fronts": "3mm Thermally Fused Laminate",
      "ends": "3mm Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "5220-N - 3mm TF Frts & Ends NAUF PB Core",
      "fronts": "3mm Thermally Fused Laminate",
      "ends": "3mm Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "6120-C - 3mm HPL Frts & Exteriors IPB CARB Compliant Core",
      "fronts": "3mm High Pressure Laminate",
      "exteriors": "3mm High Pressure Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "6120-N - 3mm HPL Frts & Exteriors NAUF PB Core",
      "fronts": "3mm High Pressure Laminate",
      "exteriors": "3mm High Pressure Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    },
    {
      "series": "6220-C - 3mm TF Frts & Exteriors IPB CARB Compliant Core",
      "fronts": "3mm Thermally Fused Laminate",
      "exteriors": "3mm Thermally Fused Laminate",
      "core": "Industrial Particleboard CARB Compliant"
    },
    {
      "series": "6220-N - 3mm TF Frts & Exteriors NAUF PB Core",
      "fronts": "3mm Thermally Fused Laminate",
      "exteriors": "3mm Thermally Fused Laminate",
      "core": "No Added Urea Formaldehyde Particleboard"
    }
  ]
}
"""

TEXT = """
You are Casework expert.
You review specification and follow the instruction to pick correct Series option which represents cabinets materials and thickness:

OPTIONS: {OPTIONS}
INSTRUCTION: {INSTRUCTION}


SPECIFICATION: {INPUT_TEXT}


You think step by step.
You markup the result option as following: 
RESULT: result series
"""


### INPUT TEXT --------------------------------------------


INPUT_TEXT_1 = """
2.3 MATERIALS, GENERAL 
A. Maximum Moisture Content for Lumber:  7 percent for hardwood and 12 percent for softwood. 
B. Hardwood  Plywood:    HPVA HP-1,  either  veneer  core  or  particleboard  core  unless  otherwise 
indicated made with adhesive containing no urea formaldehyde. 
C. Softwood Plywood:  DOC PS 1. 
D. Particleboard:  ANSI A208.1, Grade M-2 made with binder containing no urea formaldehyde 
1. Concealed Members in Music Casework:  use one of the following. 
a. Hardwood Plywood:  Seven-ply Baltic Birch. 
b. Solid Wood:  Kiln-dried hardwood, select Poplar, Fir, or mill-option lumber. 
E. MDF:  ANSI A208.2, Grade 130 Grade 130, made with binder containing no urea formaldehyde. 
F. Hardboard:  AHA A135.4, Class 1 Tempered. 
G. Plastic  Laminate:    High-pressure  decorative  laminate  complying  with  NEMA LD 3,  grades  as 
indicated or, if not indicated, as required by woodwork quality standard. 
H. Adhesives, General:  Do not use adhesives that contain urea formaldehyde. 
1. Laminate  Adhesive:    Natural  hybrid  PVA,  type  III  water-resistant  adhesives  that  cure 
through chemical reaction, containing no health or environmentally hazardous 
ingredients. 
a. Adhesive  for  Bonding  Edges:    Hot-melt  adhesive  or  adhesive  specified  above  for 
faces. 
I. Thermally Fused Laminate (TPL)  Panels:   Particleboard or MDF finished with thermally fused, 
melamine-impregnated  decorative  paper  complying  with  requirements  of  NEMA  LD3,  Grade 
VGL, for Test Methods 3.3, 3.4, 3.6, 3.8, and 3.10.  
J. Edgebanding for Plastic Laminate:   
1. Plastic  laminate  matching  adjacent  surfaces  only  where  indicated.    PVC  edge-banding, 
through  color  with  satin  finish,  3  mm  thick  at  doors  and  drawer  fronts,  1  mm  thick 
elsewhere. 
2. Barbed T-edging will not be acceptable. 
K. Edgebanding  for  Thermally  Fused  Laminate  (TFL)  Panels:    PVC  or  polyester  edge  banding 
complying with LMA EDG-1 and matching color and pattern of thermoset decorative panels. 
L. Cold-Rolled Steel Sheet:  ASTM A 1008, suitable for exposed applications. 
M. Solid-Surfacing  Material:    Homogeneous  solid  sheets  of  filled  acrylic  resin  complying  with 
ISSFA-2-01 (2002). 
1. Manufacturers:  Subject to compliance with requirements, provide products by one of the 
following: 
a. Avonite, Inc. 
b. E. I. du Pont de Nemours and Company. 
c. Formica Corporation. 
d. Samsung Chemicals (USA) Inc.; Cheil Industries Inc. 
e. Wilsonart International; Div. of Premark International, Inc. 
2. Type:  Standard type, unless Special Purpose type is indicated. 
3. Colors and Patterns:  As indicated in "List of Finishes". 


2.6 CABINET FABRICATION 
A. Complete fabrication, including assembly and hardware application, to maximum extent 
possible  before  shipment  to  Project  site.    Disassemble  components  only  as  necessary  for 
shipment  and  installation.    Where  necessary  for  fitting  at  site,  provide  ample  allowance  for 
scribing, trimming, and fitting. 
B. Plastic-Laminate-Faced  Cabinet  Construction:  As  required  by  referenced  quality  standard,  but 
not less than the following: 
1. Bottoms  and  Ends  of  Cabinets,  and  Tops  of  Wall  Cabinets  and  Tall  Cabinets:    3/4-inch 
particleboard,  plastic-laminate  faced on  exposed  surfaces,  thermoset  decorative  panels 
on  semiexposed  surfaces,  unless  otherwise  noted  or  as  required  to  meet  “Performance 
Requirements”. 
2. Shelves: 
a. Exposed Locations:  1 inch thick, vertical grade plastic laminate both sides.  Color 
to match cabinet exterior plastic laminate or as selected by A/E. 
b. Semi-exposed locations:  1 inch thick, thermally fused laminate (TFL) panels both 
sides. 
c. Front and back leading edges shall be edged with flat 1mm thick impact-resistant 
PVC edging to match shelf color. 
d. Number of adjustable shelves provided, unless indicated otherwise on the 
Drawings or on the Schedule 
1) Tall cabinets 
3 up to 60 inches  5 up to 84 inches 
4 up to 72 inches  6 up to 96 inches 
2) Base cabinets 
1 up to 36 inches 
3) Wall hung cabinets 
1 up to 24 inches  3 up to 42 inches 
2 up to 36 inches  
3. Backs  of  Cabinets:    1/2-inch  particleboard,  plastic-laminate  faced on  exposed  surfaces, 
thermally fused laminate (TFL) panels on semiexposed surfaces. 
4. Drawer Fronts:  3/4-inch particleboard, plastic-laminate faced to match doors. 
5. Drawer Sides, Backs, and Bottoms:   
a. Constructed  of  minimum  1/2-inch  particleboard,  plywood,  hardwood  lumber,  or 
high-density  fiber  board;  glued  and  doweled  or  dovetail  jointed;  surfaced  with 
vertical grade laminate or melamine of balanced construction.  Bottoms 
constructed  of  minimum  1/4-inch  tempered  hardboard,  surfaced  to  match  drawer 
sides, inset and glued to four sides.  Reinforce bottoms on wide drawers with front 
to back inset stiffeners, 1  at 24  inch wide  drawers, 2 at 36  inch and 4  at 48 inch; 
glue, fasten, and seal perimeter with hot melt adhesive. 
1) Drawers: 
a) Sides,  back  and  sub  front  shall  be  particleboard,  1/2-inch  thick, 
laminated with vertical grade laminate or melamine of balanced 
construction.  The back and sub front shall be doweled and glued into 
the  sides.    Dowels  shall  be  fluted,  with  chamfered  ends  and  a 
minimum diameter of 8mm. 
b) Drawer  bottom  shall  be  particleboard,  1/2-inch  thick,  laminated  with 
vertical grade laminate or melamine of balanced construction, 
screwed  directly  to  the  bottom  edges  of  the  drawer  box.    Drawer 
bottom less than 1/2-inch thick will not be permitted. 
c) Paper  storage  drawers  shall  be  constructed  similar  except  retaining 
hood shall be included at the rear of each drawer. 
6. File  Drawers:    Construct  as  specified  above.    File  drawers  shall  have  front-to-back  and 
side-to-side hanger file capability with hanger channel for letter size files integral with file 
drawer  sides.    3/16  inch  by  1/2-inch  removable  steel  channel  to  span  side-to-side  for 
legal size hanging files. 
7. Doors:    3/4-inch  particleboard  or  MDF,  plastic-laminate  faced  may  be  provided  as 
fabricator’s option to wood drawers. 
C. Shop  cut  openings  to  maximum  extent  possible  to  receive  hardware,  appliances,  electrical 
work, and similar items.  Locate openings accurately and use templates or roughing-in diagrams 
to produce accurately sized and shaped openings.  Sand edges of cutouts to remove splinters 
and burrs. 
D. Filler  Strips:    Provide  as  needed  to  close  spaces  between  cabinets  and  walls,  ceilings,  and 
indicated equipment.  Fabricate from same material and with same finish as cabinets. 
2.7 SPECIALTY ITEMS 
A. Support  Members:    Furniture  grade,  epoxy  powder  coated  steel  or  aluminum,  of  size  and 
configuration  as  detailed,  indicated  or  required  by  “performance  standards”.    Exposed  welds 
shall be ground smooth. 
1. Cantilevered Work Top Support Bracket:  1-1/2-inch by 1-1/2-inch by 0.1046-inch (fka 12 
gauge)  steel  vertical,  welded  and  ground  smooth  to  1-1/2-inch  wide  by  2-1/2-inch  deep 
by  0.1046-inch  (fka  12  gauge)  horizontal,  of  the  overall  size  as  indicated  on  contract 
documents, or as designated by product number.  Provide molded cap inserts at wall and 
countertop fastener holes. 
2. Specialty Countertop Support:   Rakks Bracket EH series as indicated on Drawings.” 
"""



INPUT_TEXT_2 = """
PART 2 – PRODUCTS
2.1 CASEWORK FABRICATORS
A. Available Fabricators:
Subject to compliance with requirements, fabricators offering interior architectural woodwork that may be incorporated into the Work include, but are not limited to, the following:

Case Systems, Inc.
Euronique.
LSI Corporation.
PR Bean Co. LLC.
Stevens Industries, Inc. (casework has been designed around Stevens Industries Inc.)
TMI.
Local Fabricators upon approval by Architect.
B. Solid Surface Material
Corian.
Wilsonart.
Formica.
Livingstone.
2.2 MATERIALS
A. General:
Provide materials that comply with requirements of the AWI quality standard for each type of woodwork and quality grade specified, unless otherwise indicated.

B. Wood Products:
Comply with the following:

Particleboard: ANSI A208.1, Grade M-2 M-2-Exterior Glue (at wet sink areas).
C. High-Pressure Decorative Laminate:
NEMA LD 3, grades as indicated, or if not indicated, as required by woodwork quality standard.

Available Manufacturers: Subject to compliance with requirements, manufacturers offering high-pressure decorative laminates that may be incorporated into the Work include, but are not limited to, the following:
Formica Corporation.
Nevamar.
Wilsonart International; Div. of Premark International, Inc.
D. Adhesive for Bonding Plastic Laminate:
PVA.

Adhesive for Bonding Edges: Adhesive specified above for faces.
2.3 CABINET HARDWARE AND ACCESSORIES
A. General:
Provide cabinet hardware and accessory materials associated with architectural cabinets, except for items specified in Division 8 Section "Door Hardware (Scheduled by Naming Products) (Scheduled by Describing Products)."

B. Hardware Standard:
Comply with BHMA A156.9 for items indicated by referencing BHMA numbers or items referenced to this standard.

C. Butt Hinges:
2-3/4-inch (70-mm), 5-knuckle steel hinges made from 0.095-inch- (2.4-mm-) thick metal, and as follows:

270 degree swing.
Semiconcealed hinges for flush doors. BHMA A 156.9, B01361.
Semiconcealed hinges for overlay doors: BHMA A 156.9 B1521.
D. Wire Pulls:
Back mounted, 4 inches (100 mm) long, 5/16 inches (8 mm) in diameter, 2-1/2 inches deep.

E. Catches:
Roller catches, BHMA A156.9, B03071, B03141 magnetic catches.

F. Adjustable Shelf Standards and Supports:
BHMA A156.9, B04071; with shelf rests, B04081.

G. Drawer Slides:
Side-mounted, full-extension, zinc-plated steel drawer slides with steel ball bearings, BHMA A156.9, B05091, and rated for the following loads:

Box Drawer Slides: 100 lbf (440 N).
File Drawer Slides: 200 lbf (890 N).
Pencil Drawer Slides: 45 lbf (200 N).
H. Door Locks:
BHMA A156.11, E07121 (where indicated). Drawer locks: BHMA A156.11, E07121. Provide locks at all drawer locations and as indicated in the drawings.

I. Grommets for Cable Passage through Countertops:
2-inch (51-mm) OD, black molded-plastic grommets and matching plastic caps with slot for wire passage, provide as indicated on drawings.

Product: Subject to compliance with requirements, provide "SG series" by Doug Mockett and Co., Inc.
J. Keyboard Trays:
Manufacturer's standard.

K. Exposed Hardware Finishes:
For exposed hardware, provide finish that complies with BHMA A156.18 for BHMA finish number indicated.
"""

INPUT_TEXT_3 = """
Part 2 Products
2.1 Approved Manufacturers
Stevens Cabinet Co., Inc., Teutopolis, IL; TMI, Inc., Dickinson, ND; Nolan Products, Inc., Knoxville, TN; LSI Corp., Minneapolis, MN; or approved substitute. The basis for the specification is Stevens Advantage 2800 Designer Series.

2.2 Core Material
Cabinet components having particleboard core materials shall be minimum 45 lb. - 48 lb. density industrial grade. The particleboard used shall have been tested under ANSI A 208.1 and or ASTM D-1037-91A standards.
Medium density fiberboard (MDF) used in high stress areas as drawer members and shall be minimum 48 lb. density and shall have been tested under ANSI A 208.2 standards.
Hardboard shall be nominal 1/4" thick, tempered, smooth two sides and shall be minimum 63 lb. density.
2.3 Surface Materials
Cabinet:
All exposed/semi-exposed surfaces shall be color matching thermofused or high pressure laminate. Color and pattern shall be same on both panel faces with balanced construction, and shall be chosen from a full range of WilsonArt or Formica standard finishes. Laminate shall become homogenous, thermofused to core face resulting in a unitized structure. Lamination shall be under precision controlled press cycle using high pressures of 350-400 Pounds per Square Inch (PSI) and thermosetting temperatures of 380-400 degrees F. Resin impregnated decorative faces shall be thermofused and chemically cross linked within laminate face and to core structure. Surface texture finishes to be formed against precision engraved chrome press plates. Laminates shall be tested under National Electrical Manufacturers Association (NEMA) LD3-2005 Vertical Grade GP-28 standards. Laminates shall be warranted for life against delamination. All non-exposed interior surfaces shall be thermofused melamine laminate. It is not a requirement that the non-exposed interior surfaces match the exposed and semi-exposed surfaces.

Door and Drawer fronts:
Shall be balanced construction, finished entirely in matching high pressure laminate materials on both the fronts and backs or the doors and drawers. While the rest of the exposed/semi-exposed cabinet components may be either color matching thermofused or matching HPL, the door and drawer fronts must be matching high pressure laminate on both sides.

2.4 Edgings
Door and Drawer Fronts: Edges shall have 3mm radius extrusion banding. 3mm pattern selection from Stevens Advantage 3mm Edge Selector. Fronts shall have radius edges and corners applied utilizing automated hot melt adhesive application and trimming.
Cabinet Edges: Cabinet sides, top, bottom, adjustable shelves, and other interior components shall be edged with (.020") flat edge extrusion. Automated hot melt adhesive application and trimming.
Drawer Components: 3/4" sides shall be edged with (.020") flat edge extrusion. Automated hot melt adhesive application and trimming.
2.5 Hardware
Hinges:
Shall be fully concealed type for reveal overlay and permit 176-degree door swing. Hinge crank shall be heavy-duty steel with a concealed integral self-closing spring mechanism and hinge boss shall be heavy-duty die-cast steel. Nylon expansion inserts shall be provided in door for positive screw attachment. Hinge attachment to sides shall employ special 5mm thread fasteners for maximum strength. Hinges shall incorporate mounting features providing three-dimensional adjustment and have the lifetime guarantee as warranted by the manufacturer. Doors less than 48" in height shall have two (2) hinges per door, doors, 40" to 63" in height shall be three (3) hinges per door, and all doors over 63" in height shall have four (4) hinges per door.

Door Catches:
Shall be heavy duty spring loaded, large diameter (17.5mm) roller catches mounted at door bottom. Doors over 48" shall have catch at both top and bottom. Catch strike plate shall be injection molded with integral molded engagement ridge and wide face bumper door stop.

Pulls:
Back mounted, easy grip 128mm, 5" long, Matte Nickel.

Drawer Slides:
Extension slides shall be bottom and side mount epoxy steel slides. Lateral stability achieved through a formed captive slide profile. Slides shall glide on nylon rollers and carry a 100# dynamic load rating. Slides feature both in and out drawer stop with 3" self close and adjustable cam side alignment. Slides shall also be tested under The Scientific Equipment and Furniture Association (SEFA) 6.5 Drawer Cycle Test.

Shelf Supports:
Adjustable shelf supports shall be injection molded clear polycarbonate. Supports shall incorporate integral molded lock tabs to retain shelf from tipping or inadvertent lift out. Supports shall have 5mm diameter double pin engagement into precision bored cabinet vertical hole patterns. Adjustment shall be (32mm) 1 1/4" spacings. Supports shall have a compression ridge effecting force against shelf edge to maintain positive pin engagement. Supports shall have molded-in screw attachment feature. Static test load shall exceed 200# per clip. Shelf spans above 27" shall have 5-point support with backs drilled to receive a mid-span shelf support, further reducing deflection. Shelf spans below 27" shall have end 4-point support.

Locks:
High security 6-tumbler lock system shall be provided where indicated on drawings. Locks shall have diecast body with dead bolt engagement tang. (Cylinder locks with attached rotating cams not acceptable.) Locks shall have removable and interchangeable 6-tumbler core for easy field and customer re-keying options. Locks shall be master keyed and available key-alike or key-different with 250 standard key changes. Each lock provided with a double bit key and face of lock stamped with key number.

2.6 Work Surfaces
Countertops shall be high pressure decorative plastic laminate, thermoset to core using catalyzed Polyvinyl Acetate (PVA) glue with minimum average pressure of 80 PSI and average 180 degree F. temperature. Decorative laminate shall meet NEMA LD3-2005 PF-42 (.042") specification standards.
Laminate tops shall be 1 1/16" thick with solid particleboard core structures and laminated with backer sheet. Moisture Resistant cores shall be used at all wet locations. 90 degree postform seamless front edge with matching applied backsplash.
Backsplashes and endsplashes shall be provided as indicated on drawings and shall be surfaced with same laminate as top.
Continuous tops shall be joined with minimum number of splice joints and aligned with tight joint fasteners as required to provide a uniform and gapless joint.
2.7 Component Details & Construction
Fronts:
Door and drawer fronts shall be 3/4" thick. Fronts shall be edged with 3mm radius edge extrusion with face laminate as described in 2.01.B. Automated hot melt adhesive application and trimming.

Wall Cabinets:
Components shall be 3/4" thick members throughout. Wall cabinet tops and bottoms shall include back groove and minimum four (4) dowel pins per joint for insertion into cabinet ends. Wall cabinet ends shall be 3/4" thick with back groove and precision Computer Numerical Control (CNC) drill pattern for accurate location of fixed members, hardware, and shelf supports. Wall cabinets to have two (2) integral (dowel into end) mounting frames. (Designs with simple spacer rails or rails without dowel pin engagement into ends are not acceptable.)

Mounting Frames:
Incorporated in wall units, tall units, and base units, shall be 3/4" thick with minimum two (2) dowel pins per mounting frame end joint for wall and tall units. Base units shall have a minimum of three (3) dowel pins per mounting frame end joint.

Tall Cabinets:
Components shall be 3/4" thick members throughout. Tall cabinet tops and bottoms shall include back groove and up to eight (8) total dowels per end joint (based on cabinet depth). Tall cabinet ends shall be 3/4" thick with back groove and precision CNC drill pattern for accurate location of fixed members, hardware, and shelf supports. Tall cabinets to have two (2) integral (dowel into end) mounting frames. (Designs with simple spacer rails or rails without dowel pin engagement into ends are not acceptable.)

Base Cabinets:
Components shall be 3/4" members throughout. Base unit bottoms shall incorporate back groove and up to eight (8) dowel pins per end joint (based on cabinet depth). Base units shall have a wide top and back frame feature. A wide frame in the flat horizontal plane at cabinet front with minimum three (3) dowels per end joint provides stable squaring of the top area. A second wide frame in the vertical plane behind back provides stable side-to-side rack resistance. Construction shall provide lateral and vertical stability. Open rear top area allows for easy wall mounting and ease of installation of mechanical services. (Sub tops without horizontal and vertical plane ridged frame members not acceptable.) Base cabinet ends shall be 3/4" thick with back groove and precision CNC drill pattern for accurate location of fixed members, hardware, and shelf supports.

Toe Kicks:
Separate exterior grade plywood ladder-base. Cabinet sides shall not extend to the floor.

Cabinet Backs:
Shall be in an integrated system of a 1/4" prefinished Medium Density Fiberboard (MDF) back captured in side and horizontal grooves. Unit back to be further integrated with attachment to 3/4" doweled-in mounting frames. Fixed backs are mechanically fastened into grooves and sealed with hot melt adhesive. Removable backs shall be set in groove and attached with screws.

Adjustable Shelves:
Shelves shall be 3/4" thick. Shelving shall have end 4-point support for spans under 27". Spans above 27" shall have 5-point support with backs drilled to receive additional mid-span shelf support, reducing deflection under heavier loads.

Drawers:
Four (4) sided full box design with separate attached front shall be provided. Drawer members shall be 3/4" thick with dowel pin construction at all four (4) corners. Drawer bottoms shall be 1/4" MDF trapped in groove four (4) edges as well as mechanically fastened. Entire drawer box to be Stevens Advantage TF laminated. (Drawers utilizing 1/2" members or with overlay applied bottoms, non-captured groove, or staple joint construction not acceptable.)

File Drawers:
Shall have formed cold roll 16 gauge metal sides. Sides shall be powder coated and include formed in file hanger rails. Optional cross bar file hanging adapters to be provided where legal or special hanging files are specified. File drawers shall be suspended on full extension ball bearing side mounted slides. Full extension ball bearing suspensions shall be BIFMA 120# load rated slides.

2.8 Custom Millwork and Reception Desks
Build all custom millwork items, excluding the casework per AWI Custom grade construction standards.
Holes should be routed in the studs of the reception desk for wire management.
All vertical grade surfaces should be GP28 premium grade plastic laminate. All horizontal surfaces should be GP50 plastic laminate.
All field joints must be laminated to resist moisture and allow for tighter seam installation.
Exterior grade plywood should be used at all locations where the custom millwork desk(s) contact the floor.
All millwork should be constructed in a climate controlled environment to minimize potential expansion and contraction conditions.
All parts should be cut using CNC computer software and machinery to assure consistent part sizes.
All glues used should have a minimum of at least 30% rubber contact for increased laminate adhesion.
"""

INPUT_TEXT_4 = """
PART 2 - PRODUCTS
2.1 PLASTIC LAMINATE FACED CASEWORK MANUFACTURERS
Manufacturers for Plastic-Laminate-Faced Manufactured Casework: Subject to compliance with requirements, provide products by one of the following:
Basis-of-Design Product: Casework as manufactured by Stevens Industries; Stevens Advantage.
Other Manufacturers: Manufacturers list below are required to meet requirements set forth in this Section. Manufacturing procedures may need to be modified for compliance and technical data on casework construction must be submitted for verification. Other manufacturers include, but are not limited to:
TMI Systems Design Corporation.
Case Systems.
Precision Craft.
Comparable products from other manufacturers, not listed, that meet specified requirements will be considered. Submittals for comparable products will only be considered prior to bidding. Products acceptable to the Architect will be set forth by Addendum.
2.2 PLASTIC-LAMINATE-CLAD CASEWORK
Drawings indicate sizes, configurations, and finish material of manufactured wood casework from Stevens Industries. Refer to drawings for cabinet sizes. Models selected include, but are not limited to, the following:
Base Cabinet (123200.A01): Provide casework
Cubicle Base Cabinet with Trays (123200.A03).
Unit shall be plastic laminate clad with two doors, two fixed vertical dividers, and removable horizontal hardboard dividers which create 60 compartments. Furnish each units with 60 tote trays. Tote trays shall be approximately 10 inches wide by 3-1/2 inches high by 19 inches deep.
Basis of Design: Steven's Advantage model #10263.
Translucent Tote tray size: 10" W x 3.5" H x 19" D.
Open Bottom Base Cabinet (123200.A09).
Sink Base (123200.A10).
Tall Cabinet (123200.A21).
Tall Cabinet with Adjustable Shelves(123200.A21): Premanufactured unit fabricated to sizes indicated. Unit shall be plastic laminate clad and with two doors, a center divider and five shelves, one of which is fixed and the other four adjustable.
Basis of Design: Steven's Advantage model #25129.
Wall Cabinet (123200.A31).
Unit shall be plastic laminate clad and consist of one or two doors where indicated, and five shelves, one of which is fixed and the other four adjustable. Unit shall be lockable.
Fabricator and installer shall coordinate with electrical outlet installation to provide access to wall outlets within cabinetry.
Filler (123200.A81).
Source Limitations: Obtain plastic-laminate-faced cabinets from single manufacturer.
2.3 MATERIALS, GENERAL
Maximum Moisture Content for Lumber: 7 percent for hardwood and 12 percent for softwood.
Softwood Plywood: DOC PS 1, with no added formaldehyde (NAUF).
Particleboard: ANSI A208.1, Grade M-2, with no added formaldehyde (NAUF).
MDF: ANSI A208.2, Grade 130, with no added formaldehyde (NAUF).
Plastic Laminate: High-pressure decorative laminate complying with NEMA LD 3.
Colors: Refer to Material Finish Legend on drawings for basis of design products.
Thermoset Decorative Panels: Particleboard or MDF finished with thermally fused, melamine-impregnated decorative paper complying with LMA SAT-1.
Edge Banding for Plastic Laminate: Rigid PVC extrusions, through color with satin finish, 3 mm thick at doors, drawer fronts and laminate countertops, 1 mm thick elsewhere.
3mm edge banding shall be machine-applied and set with hot-melt glue.
Edge banding colors shall match a solid color of adjacent laminate surface, unless noted otherwise, as selected by Architect. Colors shall not be limited to casework manufacturer's standard stocked colors, but will be selected by Architect from any color group offered by Panolam, Rehau and Doellken-Woodtape.
Edgebanding for Thermoset Decorative Panels: Unless otherwise specified, provide PVC or polyester edge banding complying with LMA EDG-1 and matching thermoset decorative panels.
Adhesives: Use adhesives that meet the testing and product requirements of the California Department of Public Health's "Standard Method for the Testing and Evaluation of Volatile Organic Chemical Emissions from Indoor Sources Using Environmental Chambers."
2.4 CABINET MATERIALS
Exposed Cabinet Materials:
Plastic Laminate: Grade HGS for horizontal surfaces and VGS for vertical surfaces.
Unless otherwise indicated, provide specified edge banding on all exposed edges.
Semiexposed Cabinet Materials:
Plastic Laminate: Grade VGS.
Provide plastic laminate for semi-exposed surfaces unless otherwise indicated.
Color for backs of doors and drawers shall match a solid color of that of cabinet box interior, as determined by Architect. Facings shall be balanced as required by AWI construction guidelines for grade level indicated.
Unless otherwise indicated, provide specified edge banding on all semi-exposed edges.
Concealed Cabinet Materials:
Thermoset decorative panels.
2.5 DESIGN, COLOR, AND FINISH
Design: Provide manufactured wood casework of the following design:
Flush overlay.
Thermoset Decorative Panel Colors, Patterns, and Finishes: As selected by Architect from casework manufacturer's full range.
Plastic-Laminate Colors, Patterns, and Finishes: As indicated by manufacturer's designations on Drawings.
PVC Edgebanding Color: As selected from casework manufacturer's full range, including pre-formulated colors.
Solid Surfacing: As noted on drawings. Where not specifically indicated, as selected by Architect from manufacturer's full range.
2.6 CABINET FABRICATION
Plastic-Laminate-Faced Cabinet Construction: As required by referenced quality standard, but not less than the following:
Assembly method for cabinets shall utilize "European" assembly screws (threaded steel dowel pins), similar to Hafele "Confirmat". At manufacturer's option, alternate doweled assembly methods may be used if in accordance with AWI guidelines and requirements for grade level indicated.
Cabinets boxes below sinks shall be fabricated from plywood and shall receive white plastic laminate on the interior.
Bottoms and Ends of Cabinets, and Tops of Wall Cabinets and Tall Cabinets: 3/4-inch particleboard, plastic-laminate faced on exposed surfaces, thermoset decorative panels on semi-exposed surfaces.
Shelves: Thermoset decorative panels; 3/4-inch thick for spans up to 32 inches and 1-inch thick for spans up to 48 inches.
Open Shelves: 3/4-inch particleboard, plastic-laminate faced on exposed surfaces for spans up to 32 inches and 1-inch thick for spans up to 48 inches.
Backs of Cabinets: 1/2-inch particleboard or 1/4-inch MDF, plastic-laminate faced on exposed surfaces, thermoset decorative panels on semi-exposed surfaces. Backs shall be captured in a 1/2-inch dado and set back 3/4-inch to accommodate 3/4-inch thick nailers.
Drawer Fronts: 3/4-inch particleboard, plastic-laminate faced exposed face and balanced backer.
Drawer Sub-fronts, Sides and Backs:
1/2-inch single species solid-wood or veneer-core hardwood (Birch) plywood, with glued dovetail or multiple dowel joints.
1/2-inch, high density fiberboard, 55 pcf density minimum. All parts glued and mechanically fastened using thermosetting fasteners.
1/2-inch, high density melamine composite panels. All parts glued and mechanically fastened using thermosetting fasteners.
Fabricate file drawers and lateral file drawers of width and depth necessary to accommodate hanging file rack system.
Drawer Bottoms: 1/4-inch thermoset decorative panels glued and dadoed into front, back, and sides of drawers. Use 1/2-inch material for drawers more than 24 inches wide.
Doors: 3/4-inch particleboard or MDF, plastic-laminate faced.
Removable Backs: Provide backs that can be removed from within cabinets at utility spaces.
Cabinets Bases: Bases shall be fabricated separate from cabinets (not integral). Fabricate from 3/4-inch exterior marine grade plywood or preservative-treated 2x4's with marine-grade plywood face. Fabricate in a ladder configuration with plywood fronts and back running continuous for the length of the cabinet. Provide ends, and provide additional runners centered in all cabinets greater than 24 inches wide.
Filler Strips: Provide as needed to close spaces between cabinets and walls, between cabinets and floors, ceilings, and indicated equipment. Fabricate from same material and with same finish as cabinets.
Provide top and bottom fillers and corner panels to close gaps and openings.
2.7 CASEWORK HARDWARE AND ACCESSORIES
Hardware, General: Unless otherwise indicated, provide manufacturer's standard satin-finish, commercial-quality, heavy-duty hardware.
Use threaded metal or plastic inserts with machine screws for fastening to particleboard except where hardware is through-bolted from back side.
Provide caps on fasteners at cabinet interiors in color to match adjacent cabinet finish color.
Frameless Concealed Hinges (European Type): 120 degrees of opening, self-closing. Provide two hinges for doors less than 48 inches high, and provide three hinges for doors more than 48 inches high.
Basis-of-Design: Blum #71T5580 hinges and Blum hinge plate #174H7100E.
Pulls:
Solid aluminum or chrome-plated wire pulls, fastened from back with two screws. Provide 2 pulls for drawers more than 24 inches wide.
Basis of Design: Provide Hafele "116.05.931" matt aluminum handle.
Diameter: 128mm.
Door Catches: Zinc-plated, dual, self-aligning, permanent magnet catch. Provide 2 catches on doors more than 48 inches high.
Drawer Slides: BHMA A156.9, Type B05091.
Heavy Duty (Grade 1HD-100): Side mounted; full-extension type; zinc-plated, steel ball-bearing slides. Provide with manufacturer's standard metal rear brackets as applicable.
Basis-of-Design: GSlide Corporation/Knape & Vogt Mfg. Co.; #GS4200.
Hanging File Rails: Manufacturer's standard hanging file rail system. Provide integral system at all base cabinet drawers with dimensions that will accommodate hanging files.
At 36" wide base file cabinets, provide rails on front and back for standard legal side filing. Provide two (2) removable crossbars per drawer for optional letter/legal front-to-back filing.
Adjustable Shelf Supports: 2-pin locking plastic shelf rests complying with BHMA A156.9, Type B04013.
"""

INPUT_TEXT_5 = """
"PART 2 - PRODUCTS
2.1 GENERAL
Educational casework shall meet or exceed the requirements for Architectural Woodwork Institute Quality Standards Section 400B and 1600B for premium grade reveal overlay constructed casework. Specific requirements set forth within this specification shall take precedence over the AWI Standard.
2.2 MANUFACTURERS
Manufacturers:
Case Systems: www.casesystems.com.
TMI Systems Design Corporation: www.tmisystems.com.
Stevens Industries: www.stevensind.com.
Substitutions: See Section 01 6000 - Product Requirements.
2.3 EDUCATIONAL CASEWORK
Educational Casework:
Basis of Design: Stevens Industries; 1200 Tradition.
2.4 MATERIALS
Laminated Plastics/Finishes:
High-pressure plastic laminate, .028 inch (.71 mm) in thickness, for exterior surfaces shall meet NEMA LD3-2000 VGS standards including thickness.
Provide products/colors listed in Room Finish Plan, Room Finish Schedule and Materials List as shown on drawings.
Plastic Laminate Balancing Sheet: White high-pressure cabinet-liner, .020 inch (.051 mm) in thickness shall meet NEMA LD3-2000 CLS standards. Use for balancing exterior surface laminates
Pressure Fused Laminate:
Melamine resin impregnated, 85 gram PSM average, thermofused to core under pressure.
Shall meet NEMA LD3-2000 VGL standards and NEMA LD3-2000 CLS standards, except thickness.
Locate pressure fused laminate for all cabinet interiors behind door and drawers.
Interior Color: White.
Shall be balanced at all concealed surfaces with same thermofused melamine. Unsurfaced coreboard or simple backers not allowed.
High Performance Core:
Shall be particleboard, minimum 47 lb. (21.3 kg) density, of balanced 3-ply construction with moisture content not to exceed 8%. Particleboard shall conform to ANSI A208.1-1999, Grade M-3.
Cabinet components shall be of the following minimum core thickness:
1/2-inch (12.7 mm): cabinet backs, drawer body, and drawer bottoms.
3/4-inch (19.1 mm): door and drawer face, base, wall, and tall cabinet tops and bottoms, cabinet sides, drawer spreaders, cabinet back rear hang strips, structural dividers, exposed cabinet backs, and shelves in cabinets.
1-inch (25.4 mm): product-specific work surfaces and library stack shelving unless stack fitted with vertical divider.
Edging types. Provide one or more of the following in accordance with ""Edging Locations"":
FlatEdge PVC/ABS .020 inch (.51 mm). Solid, high-impact, purified, color-thru, acid resistant PVC/ABS edging machine-applied with hot melt adhesives, automatically trimmed face, back and corners for uniform appearance.
3 mm thick PVC/ABS. Solid, high-impact, purified, color-thru, acid resistant, pre-lamination primed edging, machine-applied with hot melt adhesives, automatically trimmed, inside/outside length-radiused for uniform appearance, buffed and corner-radiused for consistent design.
Edging Locations. Provide the above specified edging types at the following locations, of the following colors:
Door/Drawer-Front Edging: 3 mm PVC to match vertical laminate surfaces.
Cabinet body edging, including door/drawer front spacer rail: FlatEdge PVC/ABS, color matched to door/drawer face or as selected.
Interior body component edging, interior dividers and drawer body: FlatEdge PVC/ABS to match cabinet interior surface color for all edges.
Edging for shelves behind doors: FlatEdge PVC/ABS to match cabinet interior surface color for all edges.
2.5 HARDWARE
Hinges
Heavy duty, five knuckle 2 3/4 inch (69.9 mm) institutional type hinge shall meet ANSI/BHMA A156.9 Grade 1 requirements. Mill ground, hospital tip, Teflon coated
Pulls:
Wire design, LH-321, 4 inches (101.6 mm).
Stain Chrome.
Provide two (2) pulls for each drawer 24 inches in width and greater.
Sliding Door Hardware:
Frameless 1/4 inch (6.4 mm) glass sliding doors: LH 370 double track rolling door assembly.
Framed 13/16 inch (20.6 mm) thick stile and rail sliding doors: LH-372 top mounted track with dual roller hangers. Vertical adjustment for accurate alignment.
Drawer Slides:
Standard Drawers: LSI Lab Series Slide, LH-375, self-closing design, epoxy powder coated White, with positive in-stop, out-stop, and out-keeper to maintain drawer in 80% open position. Captive nylon rollers, front and rear. Minimum 100 lb (45 kg) dynamic load rating at 50,000 cycles.
File Drawers: Full extension, 3-part progressive opening slide, minimum 100 lb (45 kg), zinc plated or epoxy coated at manufacturer's option.
Provide body mounted molded rails for hanging file system for legal or letter size as indicated by manufacturer's model number. Cutting or machining of drawer body/face not allowed.
Paper Storage Drawers: Full extension, 3-part progressive opening slide, minimum 100 lb (45 kg), zinc plated or epoxy coated at manufacturer's option.
Catches: Catch shall provide opening resistance in compliance with the Americans with Disabilities Act.
Provide one top-mounted magnetic catch for base and wall cabinet door. Provide two at each tall cabinet door. Catch housing shall be molded in White. LH-340ADA.
LH-345 Roller catch for mobile cabinets.
Adjustable Shelf Supports: Shall be LH-354.1 twin pin design with anti tip-up shelf restraints for both 3/4 inch (19.1 mm) and 1 inch (25.4 mm) shelves. Design shall include slot for ability to mechanically attach shelf to clip. Load rating shall be minimum 300 lbs. (136 kg) each support without failure. Cabinet interior sides shall be flush, without shelf system permanent projection.
Wardrobe Rod: Shall be 1 1/16 inch (27 mm) rod, LH 362, supported by LH-363 flanges.
Coat Hooks:
Single coat hooks, wall mount - LH-365 Bright Zinc.
Double coat hooks, wall mount - LH-366 Bright Zinc.
Double coat hooks, ceiling mount - LH-368 Bright Zinc.
Molded Personal Pencil Drawer: High-impact 100 Polystyrene with in-stop, out-stop, and self-closing features. Provide under top mounted 100 lb (45 kg) self-closing slides. Twelve compartment drawer body, and slides, Black. Provide where indicated on plans as ""molded pencil drawer"".
Locks: Where indicated, shall be disc tumbler lock keyed alike and master keyed. Dull chrome finish.
Hinged doors and drawers National Lock No. M4 7054.
Sliding doors, 13/16 inch (20.6 mm) thick, National Lock No. M4-0057.
1/4 inch (6.4 mm) sliding panel doors, National Lock No. M2-0225.
Chain Stops shall be provided on all hinged doors adjacent to cabinets or countertops of greater depth, or adjacent to walls and shall not allow contact between the door or door pull and any adjacent surfaces.
2.6 DETAILED REQUIREMENTS FOR CABINET CONSTRUCTION
Sub-Base:
Cabinet sub-base shall be separate and continuous (no cabinet body sides-to-floor), water resistant exterior grade plywood with concealed fastening to cabinet bottom. Ladder-type job site construction of individual front, back, and intermediates, to form a secure and level platform to which cabinets attach.
Sub-base at exposed cabinet end panels shall be recessed 1/4-inch (6.4 mm) from face of finished end, for flush installation of finished base material by other trades.
Cabinet Top and Bottom:
Solid sub-top shall be furnished for all base and tall cabinets.
At cabinets over 36 inches (914 mm), bottoms and tops shall be mechanically joined by a fixed divider.
ALL EXPOSED EXTERIOR SURFACES OF CABINETS INCLUDING THE EXPOSED BOTTOM AND INTERIOR EXPOSED SURFACES FOR OPEN SHELVES SHALL HAVE HIGH-PRESSURE PLASTIC LAMINATE. SEE MATERIALS LIST FOR LAMINATE COLORS.
Cabinet Ends:
Holes drilled for adjustable shelves 1-1/4-inches (32 mm) on center.
Exposed exterior cabinet ends shall be laminated with high-pressure plastic laminate, balanced with high-pressure cabinet-liner interior surface.
Fixed And Adjustable Shelves:
Thickness shall be 3/4-inch (19.1 mm).
High-pressure plastic laminate on all exposed surfaces for open shelves.
Pressure fused laminate on all exposed surfaces for shelves behind doors.
Cabinet Backs:
Cabinet back shall be fully bound (dadoed) into sides, top, and bottom, recessed 7/8- inch (22.2 mm) from cabinet rear. Rear, unexposed, side of back shall be toenailed to cabinet body with 16 gauge twin-pin coated mechanical fasteners.
Hang rails shall be located at rear of cabinet back and fastened to cabinet sides. Provide minimum of 2 at base, 2 at wall, and 3 at tall cabinets.
Exposed cabinet backs shall be high-pressure plastic laminate balanced with high-pressure cabinet-liner.
Door And Drawer Fronts:
Laminated door and drawer fronts shall be 13/16-inch (20.6 mm) thick for all hinged and sliding doors. Drawer fronts and hinged doors shall overlay the cabinet body. Maintain a maximum 1/8-inch (3.2 mm) reveal between pairs of doors, between door and drawer front, or between multiple drawer fronts within the cabinet. CABINET DOORS TO HAVE HIGH-PRESSURE PLASTIC LAMINATE ON ALL SIDES OF DOOR.
Drawers:
Drawer fronts shall be applied to separate drawer body component sub-front.
Drawer sides shall be doweled and glued to receive front and back, machine squared and held under pressure, to set.
Drawer bottom shall be fully bound (dadoed) into front, sides, and back. Routing, in drawer body for bottom, shall receive continuous glue. Reinforce drawer bottoms with 1/2-inch (12.7 mm) x 4-inch (101.6 mm) front-to-back intermediate underbody stiffeners, mechanically fastened. One at 24 inches (610 mm), two at 36 inches (914 mm), and over.
Paper storage drawers shall be fitted with full width hood at back.
Vertical and Horizontal Dividers: One of the following as indicated by cabinet number:
Natural hardboard 1/4-inch (6.4 mm) thick, smooth both faces. Secured in cabinet with molded plastic clips.
Particleboard, 3/4-inch (19.1 mm) thickness. Secured in cabinet with molded plastic clips or dowels.
Pressure Fused laminate 3/4-inch (19.1 mm) thickness. Sub-dividers secured in cabinet with molded plastic clips or dowels. Structural dividers in cabinets over 36 inches (914 mm) wide secured in cabinet with mechanical euro fasteners.
Door/Drawer Front Rail: Provide minimum 3/4-inch (19.1 mm) x 6 inch (152 mm) x full width cabinet body rails immediately behind all door/drawer and multiple drawer horizontal joints to maintain exact body dimensions, close off reveal, and be locator for lock strikes. Rail shall extend to cabinet back when keyed differently locks are specified, between multiple drawers, or drawer/door conditions.
ADA, Americans with Disabilities Act Requirements: The following special requirements shall be met, where specifically indicated on architectural plans as ""ADA"", or by General Note. Shall be in compliance with Federal Register Volume 56, No. 144, Rules and Regulations:
Countertop height: With or without cabinet below, not to exceed a height of 34 inches (864 mm) A.F.F., (Above Finished Floor), at a surface depth of 24 inches (610 mm).
Knee space clearance: Shall be minimum 29 inches (737 mm) A.F.F. at apron, and 30 inches (762 mm) clear span width.
12 inch (305 mm) deep shelving, adjustable or fixed: Not to exceed a range from 9 inches (229 mm) A.F.F. to 54 inches (1372 mm) A.F.F.
Wardrobe cabinets: Shall be furnished with rod/shelf adjustable to 48 inches (1219 mm) A.F.F. at a maximum 21-inch (533 mm) shelf depth.
Sink cabinet clearances: In addition to above, upper knee space frontal depth shall be no less than 8 inches (203 mm), and lower toe frontal depth shall be no less than 11 inches (279mm), at a point 9 inches (229 mm) A.F.F., and as further described in Volume 56, Section 4.19.
K. Workmanship:
All exposed exterior cabinet surfaces shall be .030-inch (.76 mm) high-pressure laminate. Laminate surface/ balancing liner to core under controlled conditions by approved and regulated laminating methods to assure a premium lamination. Natural-setting hybrid P.V.A. Type III water resistant adhesives that cure through chemical reaction, containing no health or environmentally hazardous ingredients, are required. Methods requiring heat are not allowed; ""contact"" methods of laminating are not allowed.
Cabinet parts shall be accurately machined and bored for premium grade quality joinery construction using dowel and screw assembly methods.
Back panel shall be fully bound (dadoed) into, and recessed 1 inch (22.2 mm) from the back of cabinet sides, top, and bottom to insure rigidity and a fully closed cabinet. Cabinet back shall be mechanically fastened from rear of body for tight interior fit and sealed with full-perimeter high-strength hot-melt adhesive.
Drawer bottom shall be fully bound (dadoed) and glued into and recessed 1/2-inch (12.7 mm) up from the bottom of sides, back, and sub-front. Sides of drawer shall be doweled to receive drawer back and sub-front. 5. 3/4-inch (19.1 mm) thick hang rails shall be mechanically fastened to end panels of
all wall, base, and tall cabinets for extra rigidity and to facilitate installation.
6. All cases shall be square, plumb, and true.
7. Case body and drawer workmanship and quality of construction shall be further
evidenced by Independent Testing Laboratory results.
8. Provide removable back panels and closure panels for plumbing access at all sink
cabinets, and where shown on drawings.
L. Mobile Cabinet Design And Construction:
1. All mobile cabinets shall be designed with a structurally layered base, to which
plate-type casters are bolted.
2. No exposed fasteners.
3. Design profile shall allow doors to swing open a full 270 degrees and overlay
cabinet sides.
4. Unit top shall be edged with 3 mm PVC/ABS and overhang case front, back, and
sides to function as a bumper system.
2.7 STEEL FABRICATIONS, ASSEMBLIES, AND SUPPORT DEVICES
A. Provide, of the size and configuration as detailed, or as indicated by product number.
Exposed welds to be ground smooth. Exposed tube ends to be capped in steel,
welded, and ground smooth.
B. Finish: Black powder coat.
C. Heavyweight Table System: Shall be constructed of 2 inch x 2 inch (50.8 mm x 50.8
mm) 12 gauge (2.66 mm) steel legs and four sided under-top surround. End
assemblies shall be factory pre-welded, with welded length-connectors for 3/8 inch
(9.53 mm) diameter double bolted 2 inch x 2 inch (50.8 mm x 50.8 mm) 12 gauge (2.66
mm) horizontal top supports. Provide levelers with non-rusting foot pad of tear drop
design, for attaching to floor, as directed by drawings. Provide leg shoes as indicated
by product designation. Work top attachment brackets shall be pre-welded to horizontal
and end frame members.
D. C-Frame Bench and Table Assemblies: Shall be constructed of 1 1/2 inch (38.1 mm)
wide x 2 1/2 inch (63.5 mm) deep 12 gauge (2.66 mm) steel tube, corner welded, and
ground smooth. Provide 3/8 inch (9.5 mm) diameter levelers with non-rusting foot pads.
Horizontal connectors shall be 1 1/2 inch x 1 1/2 inch (38.1 mm x 38.1 mm) 12 gauge
(2.66 mm) bolted to vertical C-frames. Table frames with laminate back panel
horizontal connectors shall incorporate 1 inch x 1 inch (25.4 mm x 25.4 mm) channel, to
receive panel.
E. Table Frame Cabinet Hanging System: Provide 12 gauge (2.66 mm) rolled-channel
horizontal top member and tubular horizontal lower cabinet standoff. Provide, for the
attachment and relocation of product designated cabinet types, at assemblies specified
or indicated by product designation.
F. Steel Support Legs at Cabinet Assemblies: Shall be 2 inch x 2 inch (50.8 mm x 50.8
mm) 12 gauge (2.66 mm) steel with welded top or side plate according to product
design. Provide 3/8 inch (9.5 mm) diameter leveler with non-rusting foot pad of tear
drop design for floor attachment, and leg shoe according to product design.
G. Cantilevered Work Top Support Bracket: Shall be of 1 1/2 inch x 1 1/2 inch (38.1 mm x
38.1 mm) 12 gauge (2.66 mm) steel vertical, welded and ground smooth to 1 1/2 inch
wide x 2 1/2 inch deep (38.1 mm x 63.5 mm) 12 gauge (2.66 mm) horizontal, of the
overall size as indicated on drawings, or as designated by product number. Provide
molded cap inserts at wall and countertop fastener holes.
H. Angular Work Top Support Bracket: Shall be factory welded 1 1/2 inch x 1/4 inch (38.1
mm x 6.4 mm) flat steel of vertical, horizontal, and angular design according to size
indicated on drawings, or designated by product number. 
 2.8 MISCELLANEOUS ITEMS
A. Touch-up Kit: Furnish complete touch-up kit for each type and color of educational
casework provided. Kit to include touch-up paint and other materials necessary to
perform permanent spot repairs to damage casework finish.
"
"""

INPUT_TEXT_6 = """
"PART 2 - PRODUCTS
2.1 MATERIALS
A. General:
1. Comply with quality and grading standards contained herein for each material.
2. Sizes noted on drawings or indicated herein for lumber are nominal unless detailed by specific
dimensions of actual size.
3. Plywood and particleboard 3/4-inch thickness unless noted or detailed otherwise.
4. Products surfaced four sides, unless noted otherwise.
B. Softwood Lumber
1. Quality standard: PS 20.
2. Grading Standard: AWI Premium grade.
3. Maximum moisture content: 6% for interior work; 10% for exterior work.
4. Species: Douglas fir.
5. Grain: Plain sliced.
C. Softwood Plywood
1. Quality standard: PS 1.
2. Grading standard: AWI Premium grade.
3. Core material: C-D Plugged INT-APA.
4. Face quality: A-B INT-APA.
5. Species: Douglas fir.
6. Ply construction: 3 ply - 3/8-inch; 5 ply - 1/2-inch; 7 ply - 3/4-inch.
D. Hardwood Lumber
1. Quality standard: FS MM-L-736C.
2. Grading standard: AWI Custom grade.
3. Maximum moisture content: 6%.
4. Species: Red Oak.
5. Painted Species at Platform C123: Birch.
6. Grain: Plain sliced.
E. Hardwood Plywood
1. Quality standard: PS51.
2. Grading standard: AWI Custom grade.
3. Core material: Fir Veneer.
4. Face veneer: Red Oak.
5. Grain: Plain sliced.
6. Ply construction: 3 ply - 3/8-inch; 5 ply - 1/2-inch; 7 ply - 3/4-inch.
F. Hardboard
1. Quality standard: PS 58.
2. Grade: Tempered.
3. Face: Both faces sanded.
4. Thickness: 1/4-inch.
2.2 ACCESSORIES AND TREATMENT
A. Contact Adhesive: FS MMM-A-130B, of type recommended by millwork manufacturer to suit application.
B. Wall Adhesive: Solvent release cartridge type, compatible with substrate, capable of achieving durable
bond.
C. Glass: clear tempered, 1/4-inch thick.
D. Bolts, Nuts, Washers, Lags, Pins, Nails, and Screws: Size and type to suit application.
E. Nails: Size and type to suit application, plain finish.
2.3 CABINETS AND COUNTERTOPS
A. General: If practical, cabinets not dependent upon job conditions shall be shop assembled.
B. Identification of Cabinet Parts by Surface Visibility:
1. Exposed Surfaces: Surfaces visible when:
a. Drawers and opaque doors (if any) are closed.
b. Behind clear glass doors.
c. Bottoms of cabinets 42 inches or more above finish floor.
d. Tops of cabinets below 78 inches above finish floor.
e. Tops of cabinets or millwork are visible from an adjacent higher elevation.
2. Semi-exposed Surfaces: Surfaces which become visible when.
a. Opaque doors are open or drawers are extended.
b. Bottoms of cabinets are more than 30 inches and less than 42 inches above finish floor.
3. Concealed Surfaces: Surfaces considered concealed when:
a. Surfaces not visible after installation.
b. Bottoms of cabinets less than 30 inches above finish floor.
c. Tops of cabinets over 78 inches above finish floor and not visible from an upper level.
d. Stretchers, blocking, and components concealed by drawers.
C. Laminate Clad Cabinets:
1. Quality Standard: AWI Section 10 - Casework, Premium Grade.
2. AWI Type of Cabinet Construction: Flush overlay design.
3. Laminate Grade for Exposed Surfaces:
a. Horizontal Surfaces other than Tops: GP-50 (0.050-inch nominal thickness).
b. Vertical Surfaces: GP-28 (0.028-inch nominal thickness).
c. Edges: GP-50 (0.050-inch nominal thickness).
4. Semi-Exposed Surfaces: Provide high pressure laminate, GP-28, including backs of doors and
drawers. Other interior surfaces of drawers may be sealed wood; reference SECTION 09 91 00 -
PAINTING.
5. Shop joints will be allowed only when the required lengths exceed the lengths of plastic regularly
available. Field joints shall be shop prepared and pre-fitted with bolt-up type fasteners.
6. PVC edging banding will not be acceptable.
7. The use of LPDL (Melamine) will not be acceptable.
8. Plastic Laminate: General purpose grade, high pressure decorative laminate meeting the physical
requirements of NEMA LD 3 and with a suede finish. Colors shall be as selected by Architect from
manufacturer's full color and pattern range. Architect reserves the right to select one color for the
exposed surfaces of the basic components of cabinets and a different color for the following
components of cabinets: door and drawer fronts (including edges of door and drawer fronts), backs
of open shelving, and countertop and backsplash, unless shown otherwise. Product/manufacturer;
one of the following:
Formica Brand Laminate; Formica Corp.
Pionite or Nevamar; Panolam Industries
Wilsonart; Wilsonart LLC

D. Countertops:
1. Quality Standard: AWI Section 11 - Countertops.
2. Type of Top: High pressure decorative laminate complying with Premium Grade.
3. Laminate Cladding for Horizontal Surfaces: High pressure decorative laminate, HGS (0.050-inch
nominal thickness) Grade. Laminate shall be selected from one of the manufacturers listedabove.
4. Edge Treatment: Same as laminate cladding on horizontal surfaces. Plastic laminate edges shall
return across open ends of cabinets.
5. Countertops containing sinks and countertops over dishwashers shall be exterior-grade veneer core
plywood, no substitutions.
6. Joints between tops and backsplash shall be square.
7. Joint between backsplash and countertops containing sinks shall be sealed with sanitary, silicone
sealant to ensure a tight seal.
8. No joints shall be closer than 24 inches either side of sink cutout.
9. No joints shall occur within kneespace.
10. Seal substrate at sink cutouts with sanitary, silicone sealant.
11. PVC edging will not be acceptable.
12. The use of LPDL (Melamine) will not be acceptable.
2.4 DISPLAY CASE
A. Glass: Refer to Section 08 80 00 - Glazing.
1. Provide 1/4-inch tempered glass shelves and doors with polished edges.
2. Mount glass doors on K&V P992ZC sliding glass door assembly as indicated on drawings.
B. Hardware:
1. Provide one K&V P965KA50NP Ratchet Lock at each opening between a pair of doors.
2. Furnish shelf standards and brackets; brackets should come with rests and rubber cushions.
C. Parabolic Louver: Provide as indicated on the Drawings; Parasquare 3 louvers of acrylic as manufactured
by Scientific Lighting Products (phone 800.248.0224) with 3/4 x 3/4 inch cell size, 1/2-inch thick, and silver
colored metallic finish.
D. Finish: Stain, color to be selected by Architect from manufacturer’s standard color range.
2.5 TRANSPARENT FINISH
A. AWI Premium quality. Refer TO SECTION 09 91 00 - PAINTING with stain and sheen to be Custom Color
as selected by Architect .
2.6 SHOP FABRICATION
A. Fabricate millwork to AWI Premium standards for flush overlay construction as detailed (or as indicated in
AWI Architectural Millwork Details if details are not present).
B. Sanding/Filling
1. Perform work according to AWI.
2. Sand work smooth and set exposed nails and screws.
3. Apply wood filler in exposed nail and screw indentations and leave ready to receive applied finishes.
4. On items to receive transparent finishes, use wood filler which matches surrounding surfaces and of
types recommended for applied finishes.
C. Prime seal concealed and semi-concealed surfaces. Brush apply only.
D. Provide cutouts for plumbing fixtures, inserts, appliances, outlet boxes, and other fixtures. Verify locations
of cutouts from site dimensions. Seal edge surfaces of cutouts.
E. Before proceeding with millwork required to be fitted to other construction, obtain measurements and
verify dimensions of shop drawing details for accurate fit.
F. Fabricate millwork to dimensions, profiles, and details shown.
G. Route and groove back of flat trim members, kerf backs of other wide flat members except plywood or
veneered members.
H. Assemble millwork in mill in as large of units as practicable to minimize field cutting and fitting.
I. Miter trim joints, where required, by joining, splining, and gluing to complying with requirements for
specified grade.
J. Band exposed plywood and particleboard edges with hardwood trim, 3/8-inch x width of sheet unless
otherwise noted or shown to be trimmed with plastic or aluminum.
K. On High Pressure Laminate Work:
1. Apply laminate in full, uninterrupted sheets of maximum practical lengths. Apply backing sheets to
back side of items receiving laminate surfacing. Use decorative vertical grade laminate for cabinet
interiors.
2. Form corners and butt joints with hairline joints.
3. Do not locate joints within 24 inches of sink cut-out.
4. Cap exposed edges with laminate.
L. Construction
1. General
a. Unless otherwise indicated, construct millwork bodies, bottoms, dividers, sides, tops, shelves,
doors, drawer fronts, countertops and windowsills of 3/4-inch sheet material.
b. Use 1/2-inch thick solid lumber material for drawer sides, back and sub-front.
c. Use 1/4-inch veneer core panel product for drawer bottoms and cabinet backs, unless noted
otherwise.
2. Flush Overlay Reveals
a. Unless shown or noted otherwise, allow 1/8-inch between adjacent drawers and doors and
1/16-inch at vertical edges.
b. Allow 1/8-inch reveal at top and bottom of wall cabinets and at bottom of base cabinets.
3. Methods of Joinery
a. Provide face plates, paneled ends, and construction, glued under pressure.
b. Provide body web frames of stile plowed and stub tenoned construction.
c. Join case body members by dado or concealed dowel joints.
d. Do not use mechanical fasteners or metal clips for attachment of body members to other body
members or to web frames.
4. Base cabinets
a. Use finished end panels unless condition will be fully concealed.
b. Provide unfinished toe space, prepared to receive base by others.
c. Construct drawers with Lock Shoulder rabbited (tongue-and-groove) construction.
5. Wall cabinets
a. Use finished end panels unless condition will be fully concealed.
b. Provide continuous 1x3 inches anchor cleat at top and bottom of cabinet interior full width of
unit. Secure cleat in rabbit over back, then glue and spot pin.
6. Countertops
a. Provide with 2-inch deep face edge, faced with high pressure laminate unless noted or shown
otherwise.
b. Provide loose 4-inch high pressure laminate covered splashes typically at countertops unless
taller splashes shown or noted.
c. Regardless of drawing indications, provide a 1/2-inch thick wood strip on back side of splash to
increase the splash top thickness for coping the splash to the wall.
d. Countertops containing sinks shall be medium density overlay plywood.

2.7 FINISH
A. Sand work smooth and set exposed nails.
B. Apply wood filler in exposed nail indentations.
C. On items to receive transparent finishes, use wood filler which matches surrounding surfaces and of types
recommended for applied finishes.
D. Refer to SECTION 09 91 00 - PAINTING for field applied finish descriptions.


PART 2 - PRODUCTS
2.1 MANUFACTURERS
A. Basis of Design: Manufacturer's catalog numbers for Case Systems, Inc. (website:
www.casesystems.com, phone 989-496-9510) are scheduled on the Drawings for convenience in
identifying casework components. Unless modified by notation on drawings or otherwise specified,
catalog description for indicated number constitutes requirements for each such cabinet.
B. Other Acceptable Manufacturers: Subject to compliance with requirements of this specification, equivalent
plastic-laminate-faced casework as manufactured by one of the following will also be acceptable:
LSI Corporation of America, Inc.
TMI System Design Corp.
Jericho Woodworks
Stevens Industries
Global Casework Mfg.
K.P. Kabinets, Inc.

2.2 GENERAL
A. Provide decorative laminate casework with the following minimum features:
1. M-3 47# density engineered particleboard for cabinet components.
2. PVC edges applied with hot melt.
3. Epoxy coated, self closing, minimum 150# static rated drawer slides with lifetime warranty.
4. Non-Racking, Non-Deflecting Platform Drawer Box With 1/2” Thick Bottoms.

5. 1/2"" Thick Cabinet Back.
6. “Balanced” High pressure laminates applied with rigid PVA glue.
7. Thermally Fused Laminate Interior which exceeds NEMA LD 3-1995 for GP-28 Performance.
8. Each Cabinet to have a factory applied, separate and full support toe base construction.
9. Colors and finishes shall be as selected by Architect.
10. Casework shall be independently tested to meet the following minimum performance values:
Base Unit Racking 1460 lbf
Base Front Joint Loading 725 lbf
Wall Unit Racking 1600 lbf
Wall Unit Static Load 2500 lbf
Drawer Unit Static Load 1050 lbf
Drawer Front Joint Load 805 lbf
Drawer Side Joint Load 450 lbf
11. Rail mounted casework shall be vertically and horizontally adjustable.
12. Rail mounted casework shall have integral lower leveling bar, adjustable from inside of cabinet.
B. Color and finish selections: Architect reserves the right to select one color for the exposed surfaces of the
basic components of cabinets and a different color for the following components of cabinets: door and
drawer fronts (including edges of door and drawer fronts), backs of open shelving and countertop and
backsplash, unless shown otherwise.
2.3 MATERIALS
A. Exterior Vertical Surfaces:
1. Door and drawer fronts, finished end panels, and exposed exterior backs shall be surfaced with
.028-inch thick high-pressure decorative laminate conforming to NEMA LD3-1995.

2. Exterior vertical high-pressure laminate panels shall be balanced with textured .020” thick high-
pressure cabinet liner conforming to NEMA Standard LD3-1995, CL-20. Color shall by White.

Syrface texture shall be similar to exterior finish.
3. High-pressure laminate must be laminated using a PVA adhesive, set under pressure, resulting in a
rigid glue line. Contact adhesives shall not be used.
4. HPL at open interiors, underside of wall cabinet bottoms, interiors of glazed door cabinets shall be
considered exposed and finished in Decorative High-Pressure GP-28 laminate.
B. Plastic Laminate: General purpose grade, high pressure decorative laminate meeting requirements of
NEMA LD 3 and with a suede finish. Colors shall be as selected by Architect from full color and pattern
range of plastic laminate manufacturers listed. Product/manufacturer; one of the following: 
Formica Brand Laminate; Formica Corp.
Nevamar or Pionite Decorative Laminate; Panolam Industries.
Wilsonart; Wilsonart LLC.
C. Plastic Security Glazing: GE Lexgard Laminate MPC-500 laminated polycarbonate sheet:
1. Listed as burglar resisting according to UL 752.
2. Total thickness: 0.530–inch.
3. Light Transmission: Minimum 83 percent
4. Fabrication:
a. 1/8-inch thick Lexan MR7 sheet coated with Margard surface treatment.
b. Clear, 15 mil siloxane/polycarbonate copolymer interlayer.
c. 1/4-inch thick Lexan sheet.
d. Clear, 15 mil siloxane/polycarbonate copolymer interlayer.
e. 1/8-inch thick Lexan MR7 sheet coated with Margard surface treatment.
D. Thermally Fused Interiors at Semi-Exposed Surfaces: Interior surfaces behind doors, drawer boxes,
backs, and unfinished ends shall be laminated with a White thermally fused laminate that meets or
exceeds the performance standards for NEMA LD 3-1995 for GP-28. Panels shall be of “BALANCED”
construction. Fast cycle thermally fused, melamine foil or polyester surfaced panels or other surface types
that do not meet these requirements are not acceptable.
E. 3mm PVC Edges: Door and drawer edging shall be 3mm PVC. The PVC shall be applied utilizing hot melt
adhesive and radiused by automatic trimmers. Hand tool applying and trimming of PVC shall not be
allowed. Edging shall be available in TWENTY TWO coordinated color options.
F. Adhesives:
1. Do not use adhesives that contain urea formaldehyde.
2. VOC Content for Installation Adhesives and Glues: Comply with limits when calculated according to
40 CFR 59, Subpart D (EPA Method 24).
G. Particleboard:
1. Provide product manufactured by one of thefollowing:
Kirby Forest Products
Louisiana-Pacific
Temple-Eastex
Weyerhaeuser
2. Grade M-3 Industrial, according to the American National Standard (ANSI) for Mat-Formed Wood
Particleboard, ANSI-A208.1-1993, and meeting or exceeding the following:
a. Density 47 lbs/cu.ft.
b. Moisture Content 6%
c. Modulus of Rupture 2400 psi
d. Modulus of Elasticity 450,000 psi
e. Internal Bond 80 psi
f. Hardness 900 pounds
g. Linear Expansion 0.30%
h. Thickness Tolerance +/- 0.005”
i. Face Screw Holding 325 pounds
j. Edge Screw Holding 275 pounds
2.4 CASEWORK HARDWARE AND ACCESSORIES
A. Provide manufacturer's standard, satin finish hardware units, unless otherwise indicated.
B. Hinges: Institutional type, 5 knuckle. Provide one pair for doors less than 4 ft. high and 11/2 pair for doors
over 4'. Mill ground hospital tip tight pin feature with edges eased. Hinge to be full wrap around type of
tempered steel .095"" thick. Each hinge to have minimum 9 #8 screws to assure positive door attachment.
C. Wire Pulls: Solid brass with duel chrome finish, 4"" wide, for drawers and swing doors, mounted with two
screws fastened from back. Provide two pulls for drawers over 24"" wide.
D. Door Catches:
1. Dual self-aligning, heavy-duty permanent magnet type with resistance in compliance with the
Americans with Disabilities Act and Texas Accessibility Standards. Provide two catches on doors
over 4' high.
2. At double-leaf doors, provide Ives No. 2 catch for leaf without the lock. Four screws per catch.
3. At each 1-1/8” doors, provide 1 flap stay No. 499.050.02.0215 or 499.050.03.0215 (Mepla) or
approved equivalent.
E. Drawer Slides and Accessories:
1. Standard Drawers: Case DS230, self-closing design, epoxy powder coated with positive in-stop.
Captive nylon rollers, front and rear. Minimum 100 lb. load rating.
2. File Drawers: Case DS430, full extension, 3-part progressive opening slide, minimum 100 lb., zinc
plated or epoxy coated at manufacturer's option.
3. File Drawer Rails: Case FR010, file drawer box shall have full height sides supporting the plastic file
rails for hanging file folders.
4. Paper Storage Drawers: Full extension, 3-part progressive opening slide, minimum 100 lb., zinc
plated or epoxy coated at manufacturer's option.
F. Drawer and Cabinet Locks: Provide National Lock No. C8053-14A, half-mortise type, disc tumbler locks,
round cylinder only exposed. Locks to be keyed differently, with locks in individual rooms keyed alike.
Provide a masterkey.
G. Cabinet Base Molding: Field-applied as scheduled for the adjacent walls.
H. Adjustable Shelf Supports: Provide twin pin design with anti tip-up shelf restraints for both 3/4"" and 1""
shelves. Design to include keel to retard shelf slide-off, and slot for ability to mechanically attach shelf to
clip. Load rating to be minimum 300 lbs. each support without failure. Cabinet interior sides shall be
flush, without shelf system permanent projection. Product/manufacturer; one of the following, no
substitutions:
1. SC240 Plastic Shelf Clip; Case Systems, Inc.
2. Clear Polycarbonate Shelf Clip; TMI System Design Corp.
I. Wardrobe Rod: To be 1-1/16"" rod, Knape & Vogt No. 660, supported by Knape & Vogt No. 632 CHR
flanges.
J. Shelf and Rod Hardware:
1 hanger rod KV660SS
1 shelf and rod support KV1195
2 rod flanges KV734
wood dowel connectors
K. Countertop Support Bracket: Case Systems, Inc. Model X0670
1. 11 gauge construction
2. Powder-coated finish in color as selected by Architect.
3. Load rating of 200 lbs. per lineal foot.
L. Grommets: Model No. LO-3 as manufactured by Doug Mockett & Co., Inc.
M. Molded Personal Pencil Drawer: High-impact 100 Polystyrene with in-stop, out-stop, and self-closing
features. Provide under top mounted 100 Ib self-closing slides. Twelve compartment drawer body, and
slides, Black. Provide where indicated on plans.
N. Label Holders: Provide steel with anochrome finish to hold a nominal one (1) inch by two (2) inch card.
2.5 CONSTRUCTION
A. Cabinet body components shall be secured utilizing concealed interlocking mechanical fasteners as
approved by AWI. They shall be especially designed for use in joining particleboard panels.
B. Provide tight fitting joints that will not rupture or loosen due to the following:
1. Dimensional changes in the particleboard.
2. Racking of casework during shipment and installation.
3. Normal use.
4. Fastening devices and screws shall be treated to deter or resist corrosion.
C. Construction Features:
1. Structural components: 3/4” thick with balanced surfaces.
2. Back panels: 1/2” thick surfaced both sides for balanced construction.
3. Drawer components: 1/2” thick surfaced both sides for balanced construction.
4. Mounting stretchers: 3/4” thick structural components fastened to end panels by mechanical
fasteners, and are concealed by the cabinet back.
5. Maintain a 1/8"" max. reveal between pairs of doors, between door and drawer front, or between
multiple drawer fronts within the cabinet.
6. When the rear of cabinets are exposed, a finished 3/4” thick decorative laminate back panel is
applied.
7. Exterior grade plywood core individual bases, factory applied to base and tall cabinets shall support
and carry the load of the end panels, and the cabinet bottom, directly to the floor. The base shall be
let in from the sides and back of the cabinet to allow cabinets to be installed tightly together and tight
against a wall. Also to conceal the top edge of applied rubber base molding. There shall be a front
to back center support for bases over 30” wide.
8. Horizontal parting rails between drawers: 3/4” particleboard with balanced surfaces, secured to and
further reinforcing cabinet ends. When drawers are keyed individually within a cabinet, or when
drawers are fitted with lock hasps, the parting rail shall run full depth of cabinet to preventpilfer.
9. Drill a 5mm diameter row hole pattern 32mm (1-1/4 inches) on center in cabinet ends for adjustable
shelves and for hardware mounting and replacement and/or relocation of cabinet components.
10. Door and drawer fronts and finished ends: Balanced construction with High-Pressure Decorative
Laminate (HPDL) bonded to both sides of a M-3, 47# particleboard core.
11. Doors over 30 inches wide or 80 inches high: 1-1/8 inch thick.
12. Adjustable shelves: Particleboard core, balanced surfaces and have a .020” thick PVC front edge.
Deflection limited to 1/4-inch when loaded.
a. Adjustable shelves behind doors:
1) 3/4"" thick to 27"" wide
2) 1” thick monimum for over 30"" wide.
b. Adjustable shelves in open cabinets shall be 1-inch thick, except for special use cabinets such
as mail, cubical or locker type units.Maximum tolerance for adjustable shelves: 1/16-inch at
each end.
c. Maximum tolerance for adjustable shelves: 1/16-inch at each end.
13. Fixed Interior Components: Provide fixed shelves, dividers, and cubicle compartments of full 3/4-
inch thick particleboard attached with concealed interlocking mechanical fasteners.
14. Doors: Maximum of 24 inches wide, with height not greater than the width.
D. Wall Cabinets:
1. Secure each end panel to be secured with a minimum of seven interlocking mechanical fasteners
for a total tensile strength of 2,450 pounds.
2. Wall cabinet bottoms: 1” thick particleboard core mechanically fastened to end panels and secured
to the bottom back stretcher.
3. Provide an upper 3/4"" thick stretcher behind the back panel with two interlocking mechanical
fasteners per end. Secure stretcher to the cabinet top with #8 x 2” plated flat head screws.
4. Provide a lower 3/4” thick stretcher behind the back panel and attached to the end panels with
interlocking mechanical fasteners. The stretcher is also secured to the cabinet bottom.
E. Base Cabinets:
1. Each end panel to be secured with a minimum of seven interlocking mechanical fasteners for a total
tensile strength of 2,450 pounds.
2. Base cabinets, except sink cabinets, shall have a solid 3/4” thick sub-top fastened to the ends with
interlocking mechanical fasteners.
3. Provide each kneespace to have apron with dimensions per drawings.
4. Provide 1-1/2"" thick dividers between kneespaces and adjacent spaces (e.g. dishwasher openings,
other kneespaces, etc.)
5. Provide sink cabinets with a vertically mounted front stretcher panel supporting the countertop, a
split removable back panel, and four steel corner gussets used to secure the counter-top.
6. Provide an upper 3/4” thick stretcher behind the back panel and attached to the end panels with
interlocking mechanical fasteners. This stretcher is also fastened to the full sub-stop thus capturing
the back panel.
7. Sub-Base: Factory-applied continuous, separate and fully supportive toe base for each cabinet,
constructed of preservative treated solid lumber (no cabinet body sides-to-floor) with concealed
fastening to cabinet bottom. Particleboard and untreated lumber are not permitted within inches of
the floor. Recess subbase at sides of end cabinets for rubber base installation.
F. Tall Cabinets:
1. Secure each end panel to be secured with a minimum of eleven interlocking mechanical fasteners
for a total tensile strength of 3,850 pounds.
2. Provide an intermediate fixed shelf on general storage cabinets to maintain internal dimensional
stability under heavy loading conditions.
3. Provide an upper 3/4” thick stretcher behind the back panel and attached to the end panels with
interlocking mechanical fasteners. Fastened stretcher to the full sub-stop thus capturing the back
panel.
4. Provide an intermediate 3/4” thick stretcher behind the back panel and be secured to the cabinet
ends with interlocking mechanical fasteners. Where a fixed, intermediate shelf is present, also
secure the stretcher to the shelf with a #8 x 2 plated flat head screw.
5. Drawers with 1/4” bottoms requiring hot melt glue or intermediate supports will not be permitted. NO
EXCEPTIONS.
6. Sub-Base: Provide each cabinet with a factory applied, continuous, separate and fully supportive toe
base construction (no cabinet body sides-to-floor) with concealed fastening to cabinet bottom.
Recess subbase at sides of end cabinets for rubber base installation.
G. Drawers:
1. Drawer box: Full 1/2” thick non-racking, non-deflecting platform bottom which is carried directly by
“L” shaped, bottom mount drawer glides. Secure sides with 1 1/4” long screws directly into platform
and into the sides.
2. Sides, back, sub-front and bottom: 1/2” thick 47# density particleboard surfaced both faces with
White thermally fused laminate per 2.02.B.1. The top edge shall be .020” PVC matching the drawer
color.
3. Join corners with fluted hardwood dowels and glue, minimum 32mm o/c.
4. Drawer fronts: Removable and attached drawer box sub-front with screws from inside of drawer.
2.6 PERFORMANCE
A. Laminates:
1. “High Pressure Decorative Laminates” (HPDL): Meet the definition and performance requirements
of NEMA LD3.
a. Vertical grade laminate: GP-28 balanced with a minimum grade of CL-20.
b. Countertops: GP-50.
2. Thermally Fused Laminate: Meet performance requirements of NEMA LD3 for GP-28.
B. Hinges: ANSIA156.9.4.1,2,3,4.
1. Provide two hinges mounted 23” on center on a 23-7/16” wide x 19-11/16” high cabinet door shall be
capable of supporting a 100 pound test load located 1” from the outside edge of the door.
2. Cycle, open and close, from 5 degrees open through 95 degrees open with no failure to hinges,
door, or cabinet end panel.
3. Horizontal permanent hinge set: Maximum .030”.
C. Drawers: ANSI/BHMA A156.9-1988 4.11: Test an actual production drawer box with an applied finished
front and 450mm drawer slides mounted per the manufacturers’ instructions shall be tested asfollows:
1. Dynamic Cycle Test: When uniformly loaded with 100 pounds and tested through 50,000 opening
and closing cycles, the drawer shall operate freely.
2. Static Edge Load Test: No permanent damage or distortion when the drawer is fully drawe
extended, a 150 pound load is supplied to the drawer front at a point on the centerline of the drawer
for one minute.
D. Adjustable Cabinet Shelving: Maximum deflection of 1/4-inch when loaded according to NAAWS
Standards.
2.7 COUNTERTOPS
A. HPDL Finish
1. Countertops nominal 1-1/8 inch thick
2. General Purpose, GP-50 HPDL on horizontal surface, conforming to NEMA Standard LD3.
3. Laminate bonded to 1” thick 47# M-3 particleboard core with PVA rigid adhesives. Contact method
shall NOT be allowed. Core shall be balanced with HPL backer.
4. Secure joints with adhesive and tight joint fasteners.
5. Provide 4” high back splashes where shown and at ends abutting walls and adjacent cabinets.
6. Countertops shall conform to ANSI A161.2-1979 PERFORMANCE STANDARDS FOR
FABRICATED HIGH-PRESSURE DECORATIVE LAMINATE COUNTERTOPS.
7. Do not locate joints closer than 24 inches either side of sink cutout.
8. Do not locate joints within knee spaces.
9. Countertops containing sinks, and countertops over dishwashers: Exterior-grade veneer core
plywood, NO SUBSTITUTIONS.
10. Seal joint between backsplash and countertops containing sinks, and substrate at sink cutouts, with
sanitary silicone sealant. Refer to Section 07 92 00 - Joint Sealants.

2.8 FABRICATION
A. Fabricate plastic laminate-faced casework to dimensions, profiles and details shown.
B. Shop-assemble units in as large components as practicable to minimize field jointing.
C. Install hardware uniformly and precisely after final finishing is complete. Set hinges snug and flat in
mortises unless otherwise indicated. Turn screws to a flat seat. Adjust and align hardware so that moving
parts operate freely and contact points meet accurately. Allow for final field adjustment after installation.


PART 2 - PRODUCTS
2.1 APPROVED MANUFACTURER

A. Specifications are based on Kewaunee Scientific Equipment Corp. standard construction
with certain modifications as specified herein, or Architect approved equal. Other
manufacturers must have a minimum of five (5) years experience manufacturing products
meeting or exceeding the specifications and comply with Division 01 Sections regarding
substitutions to be considered.

2.2 MATERIALS
A. General:
1. Material shall be selected so that the finished installation shall provide an attractive
and harmonious appearance.
2. Sink Supports: Sink Supports, where required, shall be of a cradle type consisting
of two 1-1/4 inch x 1-3/4 inch horizontal cleats and adjustable leveling bolts or
glides. The horizontal cleats shall be supported by two 3/4 inch x 2-1/2 inch
hardwood plywood cleats attached to the cabinet end panels, or by four 1/4"" steel
rods attached to the cabinet top frame.
3. Support Struts: Shall consist of two 16 gauge channel uprights fastened top and
bottom by two adjustable ""U"" shaped spreaders, each 12 gauge, 1-1/2 inch x length
required. Struts shall be furnished to support drain troughs, and to support work
top at plumbing space under fume hood superstructures or other heavy loads. They
shall be fabricated so as to accept industry standard, pipe and conduit hangers.
4. Other Materials: Provide other materials, not specifically described, but required
for a complete and proper installation.

2.3 WORKSURFACES
A. Materials:
1. Kemresin Epoxy Resin Tops
B. Work Top Performance Requirements:
1. Molded Epoxy Resin (Kemresin)
a. Flexural Strength (A.S.T.M. Method D790) = 15,000 PSI
Compressive Strength (A.S.T.M. Method D695) = 30,000 PSI
Hardness, Rockwell E (A.S.T.M. Method D785) = 100
Water Absorption (A.S.T.M. Method D570)%
by weight, 24 Hours = 0.04
% by weight, 7 Days = 0.05
% by weight, 2 Hour Boil = 0.04
Specific Gravity = 1.97
Tensile Strength = 8,500 PSI
b. Performance Test Results (Heat Resistance): A high form porcelain
crucible, size 0, 15 ml capacity, shall be heated over a Bunsen burner until
the crucible bottom attains an incipient red heat. Immediately, the hot
crucible shall be transferred to the top surface and allowed to cool to room
temperature. Upon removal of the cooled crucible, there shall be no
blisters, cracks or any breakdown of the top surface whatsoever.
c. Performance Test Results (Chemical Resistance): Tops shall resist
chemical attacks from normally used laboratory reagents. Weight change
of top samples submerged in the reagents* listed in the next paragraph for
a period of seven (7) days shall be less than one-tenth of one percent,
except that the weight change for those reagents marked with ** shall be
less than one percent. (Tests shall be performed in accordance with
A.S.T.M. Method D543 at 77 degrees F.).
*Where concentrations are indicated, percentages are by weight.
Acetic Acid, Glacial Iso-Octane
Acetic Acid, 5% Kerosene
Acetone Methyl Alcohol
Ammonium Hydroxide, 28% Mineral Oil
Ammonium Hydroxide, 10% Methyl Ethyl Ketone
Aniline Oil Nitric Acid, 70%**
Benzene Nitric Acid, 40%
Carbon Tetrachloride Nitric Acid, 10%
Chromic Acid, 40%** Oleic Acid
Citric Acid, 10% Olive Oil
Cottonseed Oil Phenol, 5%
Dichromate Cleaning
Solution** Soap Solution, 1%
Diethyl Ether Sodium Carbonate, 20%
Dimethyl Formamide Sodium Carbonate, 2%
Distilled Water Sodium Chloride, 10%
Detergent Solution, 1/4% Sodium Hydroxide, 50%
Ethyl Acetate Sodium Hydroxide, 10%
Ethyl Alcohol, 95% Sodium Hydroxide, 1%
Ethyl Alcohol, 50% Sodium Hypochlorite,5%
Ethylene Dichloride Sulfuric Acid, 85%
Heptane Sulfuric Acid, 30%
Hydrochloric Acid, 37% Sulfuric Acid, 3%
Hydrochloric Acid, 10% Toluene
Hydrogen Peroxide, 28% Transformer Oil
Hydrogen Peroxide, 3% Turpentine
d. Performance Test Results (Chemical Spot Tests - 24 Hours): Chemical
spot tests shall be made by applying 10 drops (approximately 1/2 cc) of
each reagent to the surface to be tested. Each reagent (except those marked
**) shall be covered with a 1-1/2 inch diameter watch glass, convex side
down to confine the reagent. Spot tests of volatile solvents marked ** shall
be tested as follows: A 1"" or larger ball of cotton shall be saturated with
the solvent and placed on the surfaces to be tested. The cotton ball shall
then be covered by an inverted 2-ounce, wide mouth bottle to retard
evaporation. All spot tests shall be conducted in such a manner that the
test surface is kept wet throughout the entire 24-hour test period and at a
temperature of 77 degrees F. + 3 degrees F. At the end of the test period,
the reagents shall be flushed from the surfaces with water and the surface
scrubbed with a soft bristle brush under running water, rinsed, and dried.
Volatile solvent test areas shall be cleaned with a cotton swab soaked in
the solvent used on the test area. Spots where dyes have dried shall be
cleaned with a cotton swab soaked in alcohol to remove the surface dye.
The test panel shall then be evaluated immediately after drying.
Ratings:
A = No effect or slight change in gloss.
B = Slight change in color or marked loss of gloss.
C = Slight surface etching or severe staining.
D = Swelling, pitting, or severe etching.
Reagents* Rating
Acetic Acid, 98% A
Acetone** A
Ammonium Hydroxide, 28% A
Carbon Tetrachloride** A
Chloroform** A
Chromic Acid, 60% C
Chromic Acid, 40% C
Dichromate Cleaning Solution*** C
Dimethyl Formamide A
Ethyl Acetate** A
Ethyl Alcohol** A
Formaldehyde, 37% A
Formic Acid, 90% A
Hydrochloric Acid, 37% A
Hydrofluoric Acid, 48% C
Hydrogen Peroxide, 28% A
Methanol** A
Methylethyl Ketone** A
Nitric Acid, 70% B
Phenol, 85% A
Phosphoric Acid, 85% A
Sodium Carbonate, 20% A
Sodium Hydroxide, 40% A
Sodium Hydroxide, 10% A
Sodium Hypochlorite, 5% A
Sulfuric Acid, 96% D
Sulfuric Acid, 85% A
Toluene** A
Wrights Blood Stain A
Xylene** A
* Where concentrations are indicated, percentages are by weight.
** Indicates these solvents tested with cotton and jar method.
*** Dichromate cleaning solution is a formula from Lange's
Handbook of Chemistry.


PART 2 - PRODUCTS
2.1 MATERIALS
A. Solid Surface Material: Samsung Staron with standard ‘setback’ edge condition as basis of
design.
1. Color to be selected from manufacturer’s full range.

2.2 ACCESSORIES
A. Joint adhesive:
1. Manufacturer’s standard one- or two-part adhesive kit to create inconspicuous,
nonporous joints.

B. Sealant:
1. Manufacturer’s standard mildew-resistant, FDA-compliant, NSF 51-compliant
(food zone - any type), UL-listed silicone sealant in colors matching components.

C. Sink/lavatory mounting hardware:
1. Manufacturer’s standard bowl clips, panel inserts and fasteners for attachment of
undermount sinks/lavatories
D. Conductive tape:
1. Manufacturer’s standard aluminum foil tape, with required thickness, for use
with cutouts near heat sources.

E. Insulating felt tape:
1. Manufacturer’s standard for use with conductive tape in insulating solid surface
material from adjacent heat source.

2.3 FACTORY FABRICATION
A. Shop assembly:
1. Fabricate components to greatest extent practical to sizes and shapes indicated, in
accordance with approved shop drawings and manufacturer’s printed instructions
and technical bulletins.
2. Form joints between components using manufacturer’s standard joint adhesive
without conspicuous joints.
a. Reinforce with strip of solid polymer material, 2 inch wide.
3. Provide factory cutouts for plumbing fittings and bath accessories as indicated on
the drawings.
4. Rout and finish component edges with clean, sharp returns.
a. Rout cutouts, radii and contours to template.
b. Smooth edges.
c. Repair or reject defective and inaccurate work


PART 2 - PRODUCTS
2.1 ACCEPTABLE MANUFACTURERS
A. Tesco Industries, LP, Bellville, Texas; (800) 699-5824, or Architect approved equal. Other
manufacturers must have a minimum of five (5) years experience manufacturing products
meeting or exceeding the specifications and comply with Division 01 Section requirements
2.2 MATERIALS
A. Catalog Standards: Model numbers listed are by Tesco Industries, Inc. Catalog
description for indicated number constitutes requirements, unless otherwise specified.
B. Wood Species:
1. All wood used in the construction of furniture and cabinets shall be northern grown
red oak and shall be selected form seasoned, kiln-dried materials free from
structural imperfections. The moisture content at time of fabrication shall range
from 5% to 7%. All woods shall be selected for uniformity of grain and color. Wood
used for internal parts shall be selected a structurally sound.
2. All plywood used shall be of quality as specified by the American Plywood
Association. All facing materials shall be no less than 1/28 inch thickness after
sanding. Face veneers (i.e. veneers facing an exterior surface) shall be select,
plain sliced, slip matched, to selected species.

C. Wood Finishes:
1. In the manufacturing process after parts are cut and ready to finish, all solid oak
panels and shelves are dipped in Nelsonite 15B02 wood stabilizer. Prior to
assembly, parts pass through a 5 head wide belt sander which has 100, 120, 150,
180, and 220 grit sand paper. Parts are then inspected, filled and hand sanded as
necessary until thoroughly cleaned.
After sanding, the parts are roll coated with 100 percent solid U.V. stain, wiped,
U.V. oven cured and then pass through a deburring station.
Then parts are roll coated with a 100 percent solid U.V. sealer, U.V. oven cured,
then passed through a final deburring station.
Next parts are roll coated with a final 100 percent U.V. clear top coat and then
U.V. oven cured.
All sealers and finishes must be U.V. and applied by a flat line roll coat system to
insure a uniform and environmentally safe finish.

2.3 CONSTRUCTION
A. Shelving:
1. All vertical uprights of library shelving shall be a minimum of 1 inch thick, kiln
dried solid oak, glued up in strips no less than 1-1/2 inches and no more than 4
inches, and free of all imperfections. Veneered plywood of any type and / or
uprights of less than 1 inch thickness will not be acceptable.
The 2 inch canopy cornice shall be constructed of an oak plywood top with solid
oak bullnose facia strips which are machine applied to front and back edges.
Bolting cleats are attached by means of wood screws and glued construction.
Continuous top shelving shall have a 2 inches deep dovetailed top frame provided
with countersunk holes for screwing down a continuous top made of solid core with
standard bullnose external solid oak edge bands or as specified in the equipment
list. Bases shall be of solid hardwood 3-1/2 inches in height with dovetail joints.
Shelving units shall be standard with back panels on single faced shelving and
divider panels on double faced units. Backs shall be 1/4 inch thick oak plywood and
finished on one side for single faced units and both sides for double faced units.
Backs shall be recessed in a dado on all sides. End panels shall be joined to
cornice and base by means of metal ferrules embedded in the end panels with 5/16
inch hex head bolts passing through the cleats on the cornice and the sides of the
base and engaging the ferrules. Filler and corner units shall be supplied as needed
to complete shelving runs as shown on the plan.
Shelves shall be a minimum of 3/4 inch thick, edge glued, solid oak strips no less
than 1-1/2 inches wide nor more than 4 inches wide. The underside of all shelves
shall be neatly routed to receive the metal supporting pins. Adjustment of shelves
shall be of pin hole style construction with adjustments at 1-1/4 inch increments,
which provides for a cleaner less conspicuous installation.
Adder shelving units shall be joined by means of 5/16 inch hex head bolts passing
through both bases and the intermediate upright, both cleats on the cornices and
the intermediate upright, and then secured with washers and nuts.
All shelving 60 inches high and under can have a continuous style top. Continuous
tops when used, shall have the standard bullnose external solid oak edge band or
an optional edge style as specified in the equipment schedule. All shelving 72
inches and higher will have a 2 inch wood veneer canopy top to match shelving
unit..
Shelf arrangements per face shall be as follows:
Height Total Shelves
42 inches 3
60 inches 4
Construct units in 36” lengths (max.) for ease of relocation.
All island shelving shall be on casters. All wall mounted shelving shall be fixed."
"""

INPUT_TEXT_7 = """
"PART 2 - PRODUCTS
2.01 CORE MATERIAL
Cabinet components having particle board core material shall be of a minimum 45 lb. density, M-2 industrial grade. The particle board used shall have been tested under ANSI A208.1 1993 standards and/or ASTMD 1037-91A.
Medium density fiberboard (MDF) shall be used in high stress areas as drawer members and shall be minimum 48 lb. density MD-21 grade and tested under ANSI A208.2 1994 Standards.
Industrial hardboard shall be pre-finished 1/4"" thickness composed of wood fibers, phenolic resin binders and moisture inhibitors that meet or exceed the hardboard product standard ANSI/AHA A135.4 1988.
All countertops located with 3'-0"" of any direction of built-in sink and/or bubblers shall be constructed of marine grade ""Greenboard"" MR moisture/water resistant particle board. The particle board shall be tested under ANSI A208.1 1-1993, M3 standards.
2.02 SURFACE MATERIAL
Exposed exteriors shall be permanently thermofused melamine laminate, fused to core using a minimum average pressure of 320 PSI and average 320 degree F. temperature. Thermofused melamine laminate shall meet ALA 1996 specification standards, as tested against the high pressure laminate NEMA LD 3-1995, VGS.028 specification standards. (Warranted for life against delamination).
Exposed doors and drawer fronts shall be permanently thermofused melamine laminate, fused to core using a minimum average pressure of 320 PSI and average 320 degree F. temperature. Thermofused melamine laminate shall meet ALA 1996 specification standards, as tested against the high pressure laminate NEMA LD 3-1995, VGS.028 specification standards, (Warranted for life against delamination).
Exposed interiors shall be permanently thermofused melamine laminate, fused to core using a minimum average pressure of 320 PSI and average 320 degree F. temperature. Thermofused melamine laminate shall meet ALA 1996 specification standards, as tested against the high pressure laminate NEMA LD 3-1995, VGS.028 specification standards. (Warranted for life against delamination).
Semi-exposed and concealed surfaces shall be permanently thermofused melamine laminate or high pressure decorative plastic laminate cabinet liner, 0.020"" thickness for balanced construction. Thermofused melamine laminate shall meet the ALA 1996 specifications standard, as tested against the high pressure laminate NEMA LD 3-1995, VGS.028 specification standards.
2.03 EDGINGS
Exposed exterior cabinet front edges shall be banded with a contrasting or matching rigid PVC extrusion, 0.020"" thickness, resistant to chip, crack and high impact. Edging shall have a satin finish with a UV cured top coat for additional durability. The 0.020"" thick edging shall be applied with waterproof hot melt adhesive.
Door and drawer front edges shall be banded with a contrasting or matching rigid PVC extrusion, 3mm (1/8"") thickness, resistant to chip, crack, and high impact. Edging shall have a satin finish with UV cured top coat for additional durability. The 3mm thick edging shall be applied with waterproof hot melt adhesive, and shaped to provide radiused edges and radiused corners.
Adjustable shelves shall be banded with PVC extrusion, resistant to chip, crack, and high impact. Edging shall have a satin finish with a UV cured top coat for additional durability. Edging shall be applied with waterproof hot melt adhesive. Shelves to be 1"" thick. 0.020"" thick PVC edging shall be applied to four (4) edges of adjustable shelf.
All other interior components, including drawers, shall be banded with a PVC extrusion, 0.020"" in thickness, resistant to chip, crack, and high impact. Edging shall have a satin finish with a UV cured top coat for additional durability. Edging shall be applied with waterproof hot melt adhesive.
2.04 COLOR SELECTIONS
Exposed cabinet exteriors shall be chosen from Thermofused melamine laminate selections as depicted in manufacturer's color selector guide. A minimum of seventy (70) colors and patterns shall be available as standard selection.
Exposed doors and drawer fronts shall be chosen from Thermofused melamine laminate selections as depicted in manufacturer's color selector guide. A minimum of seventy (70) colors and patterns shall be available as standard selection.
Semi-exposed surfaces, including drawer box components, shall be finished in either pearl or grey as selected from casework manufacturer's standard interior color selections.
Exposed interior components, including both faces of shelves and interior face of backs to match exposed cabinet exterior color selection.
Door and drawer front edges shall be chosen from one of twenty-two (22) trim group colors in 3mm thick PVC in contrasting or matching colors as depicted in manufacturer's color guide.
Exposed front edge of cabinet, including exposed interior edges, shall be selected from one of seventy (70) trim group colors in 0.020"" thick PVC in contrasting or matching colors as depicted in manufacturer's color guide, or commercial match to selected exposed exterior color based on availability.
Semi-exposed edges of cabinet components including drawers, shall be either pearl or grey in 0.020"" thick PVC.
Pulls shall be available in chrome, brass, bent wire and injection molded pulls in either bent wire or contour design, to be available in twenty (20) colors as selected from manufacturer's color selector.
Casework of substitute brands with lesser amounts or more restrictive selection requirements will not be considered equal and shall be rejected.
Finishes to be laminate manufacturer's matte, suede, or equivalent finish as approved by Architect. Samples will be reviewed by Architect for color, texture, and pattern only.
2.05 HARDWARE
Hinges
Institutional five-knuckle secured with minimum of eight screws. Hinge plate must extend into cabinet a minimum of 2 1/4"" (56 mm) in order to assure maximum strength. Finish to be powder-coated baked on black enamel or brushed chrome US26D.
Two hinges used on all doors less than 48"" (1220 mm) in height, three hinges used on all doors 48"" (1220 mm) or greater in height. Hinge to accommodate 13/16"" (21 mm) door.
Door catches shall be a heavy-duty spring loaded, large diameter (17.5mm - 11/16"") roller type catch mounted at bottom edge. All doors over 48"" in height shall be provided with roller catch at both top and bottom of door.
Catch strike plate shall be injection molded ABS, with an integrally molded engagement ridge. Strike plate shall also provide a wide face bumper insuring a positive door stop.
Pulls shall be impact resistant injection molded bent wire, 4"" length available per color selection in Article 2.04.H.
Drawer and slide out shelves shall be suspended with bottom mount, side and bottom attached nylon roller epoxy coated steel slides to ensure quiet, smooth operation. Lateral stability is achieved thru a special formed captive profile. Slides shall have 100 lb. load rating, with both in and out drawer stop, 3"" self close feature and a side adjustment cam allowing 3mm side to side alignment.
Drawers specifically noted for full extension file use shall be suspended with bottom mount, side and bottom attached nylon roller epoxy coated steel slides to ensure quiet, smooth operation. Lateral stability is achieved thru a special formed captive profile. Slides shall have 150 lb. load rating, with both in and out drawer stop, and 3"" self close feature. File drawer shall include extruded aluminum roller epoxy coated side rails to accept standard hanging file folders.
Knee-space, pencil drawers, and keyboard trays, shall be designed to permit under counter or support frame mounting, with 100 lb. nylon roller epoxy coated steel slides.
Hanger rods shall be heavy chrome plated tubing. Rod shall be securely affixed to cabinet shelves.
Tote trays shall be of high impact polystyrene with smooth edges. Each tray to include an identification card holder and shall be suspended from rails securely attached to cabinet verticals.
Shelf support clips for 1"" thick adjustable shelves shall be injection molded clear polycarbonate. Support clips shall incorporate integral molded lock tabs to retain shelf from topping or inadvertently being lifted out. Support clip shall have 5mm dia. double pin engagement into precision bored hole pattern in cabinet vertical members. Clips shall have a molded ridge which provide pressure against edge of shelving to maintain positive pin engagement. Clip shall be designed in such a manner to provide means for permanent retention to shelf. Static test load must exceed 200lb. per clip.
Dividers that are 1/4"" thick shall be fully adjustable and retained with injection molded clear polycarbonate clip.
Locks shall be cylinder type, diecast, with five (5) disc tumbler mechanism. Each lock shall be provided with milled brass key. Master key cabinets to room doors. Cabinets with multiple locks installed shall be keyed alike by room, with each cabinet in that room keyed the same unless otherwise specified. Locks shall be Remov-A-Core to give flexibility for different pass key options. Locks shall be provided on all cabinets capable of locking. Key all cabs and drawers within each room alike. Each room to be keyed differently. Provide 1 Master key for all locks. Note: Key each cabinet and drawer in Staff Lounge 152 differently with 1 Master key.
Sliding door track shall be double channel rigid PVC extrusion at both top and bottom of doors. Track shall be available in pearl, black or grey colors.
2.06 COMPONENTS
Base, wall and tall cabinet ends shall be 3/4"" thick particle board, laminated for balanced construction, surfaced as described in Article 2.02.A and edged as described in Article 2.03.A.
Base and tall cabinet tops and bottoms shall be 3/4"" thick particle board, laminated for balanced construction, surfaced as described in Article 2.02.C, and edged as described in Article 2.03.A.
Wall cabinet top and bottom shall be 1"" thick particle board, laminated for balanced construction, surfaced as described in Article 2.02.C, and edged as described in Article 2.03.A.
Vertical cabinet members shall be 3/4"" thick particle board, laminated for balanced construction, surfaced as described in Article 2.02.C, and edged as described in Article 2.03.D.
Cabinet backs shall be 1/4"" thick pre-finished industrial hardboard.
Frame rails shall be 3/4"" thick x 3 3/4"" wide particle board, laminated for balanced construction, surfaced as described in Article 2.02.C, and edged as described in Article 2.03.A.
Sub base shall consist of two (2) toe kick support rails shall be 3/4"" thick x 3 3/4"" high particle board and be inset from cabinet front and back edge, to give additional load support.
Mounting rails shall be 3/4"" thick x 3 3/4"" wide particle board. Wall cabinets shall have rails positioned at the top and bottom. Tall cabinets shall have rails positioned at the top and intermediate location. Base cabinet shall have rails positioned at the top of unit.
Drawers shall be full box design with a separate front. Drawer sides and ends shall be constructed of 5/8"" medium density fiberboard with pearl or grey color thermofused melamine laminate and matching PVC top edges. Bottoms shall be 1/4"" thick medium density fiberboard, pearl or grey color thermofused melamine laminate. All drawers to receive locks.
Adjustable shelves shall be 1"" thick. Edges of shelf shall be banded as described in Article 2.03.C with a high impact, rigid PVC extrusion, pearl or grey in color.
Sliding display doors shall be constructed of 1/4"" thick distortion free glazing sheet. Center edge shall be capped with full length aluminum channel. Aluminum channel shall be custom extruded, clear etched and anodized. Full length extruded aluminum channel shall be used on other edges.
Solid hinged doors, sliding doors and drawer fronts shall be 3/4"" thick material of balanced construction, surfaced as described in Section 2.02.B, edged as described in Article 2.03.B. All doors to receive locks.
2.07 CONSTRUCTION
Cabinet parts shall be accurately machined and precision bored for premium grade quality joinery construction, utilizing automatic machinery to ensure consistent sizing on modular cabinets. Cabinets shall be assembled under controlled case clamp conditions, assuring final cabinet squareness and proper joint compressions.
Cabinet ends shall be bored to receive 8mm, industrial grade hardwood laterally fluted dowels with chamfered ends. Cabinet ends shall be prepared to receive adjustable shelf hardware at 32mm (approximately 1 1/4"") centers. Door hinges and drawer slides shall be machined drilled to maintain vertical and horizontal alignment of components. Inset grooving with chamfer shall be machined 3/4"" from rear edge to accept the 1/4"" back. Base and tall units shall have one piece end panels continuous to floor for added load capabilities.
Tops and bottoms shall be joined to cabinet ends using a minimum of six (6) dowels at each joint for twenty-four (24) inch deep cabinets and a minimum of four (4) dowels at each joint, for twelve (12) inch deep cabinets. All dowels to be industrial grade hardwood, laterally fluted, with chamfered ends and 8mm in diameter. Top of base cabinet will be full depth. Inset grooving with chamfer shall be machined 3/4"" from rear edge to accept the 1/4"" back.
Vertical dividers shall be bored to receive adjustable shelf hardware at 32 mm (approximately 1 1/4"") centers. Dividers shall be joined to tops and bottoms with 8mm diameter hardwood dowels.
Frame rails shall be joined to ends with 8mm diameter hardwood dowels.
Two (2) toe kick supports shall be inset from cabinet front and back edges, and doweled into cabinet ends with 8mm hardwood dowels.
Mounting rails shall be fully concealed behind backs. Rails shall be 3/4"" thick and fastened to cabinet ends with 8mm hardwood dowels. Wall and tall cabinet shall incorporate two mounting rails. Wall cabinets shall have rails positioned at top and bottom. Tall cabinets shall have rails positioned at top and intermediate location. Base units shall have rail positioned in the upper back area.
Back panels shall be 1/4"" thick and inset 3/4"" from rear edge of cabinet. Back shall be glued and continuously trapped in top, bottom and ends of cabinets.
Drawer corner joints shall be interlocking dowel pin design. Hardwood dowel pins, 8mm diameter shall be inserted into drawer fronts and backs to fit into machined hole patterns in drawer sides. Bottoms shall be trapped into grooves on all four sides glued and mechanical fastened. Drawers shall be suspended on slides as described in Article 2.05.E.
2.08 WORK SURFACES
Core material having particle board shall be of a minimum 45 lb. density, M-2 industrial grade. The particle board used shall have been tested under ANSI A208.1 1993 standards and/or ASTMD 1037-91A.
Surface material shall be high pressure decorative plastic laminate thermoset to core using catalyzed PVA glue with a minimum average pressure of 90 PSI and average 180 degree F temperature. High pressure decorative plastic laminate shall meet NEMA LD 3-1995, HGP.039 specification standards.
Color selection shall be high pressure decorative plastic laminate selections as depicted in manufacturer's color selector guide. A minimum of seventy (70) colors and patterns shall be available as standard selection.
Exposed edges shall be 90 degree plastic laminate with a chamfered edge.
Underside of all work surfaces to have BK-20 backer or approved equivalent. This balance sheet shall be thermoset to core using catalyzed PVA glue with a minimum average pressure of 90 PSI and average 180 degree F temperature.
Counter Tops - Solid Surface (by others)
Physical Properties shall meet minimally:
Flexural Strength ASTM-Method D-790 16,000/psi
Compressive Strength ASTM-Method D-695 36,500/psi
Hardness Rockwell M ASTM-Method D-785 110
Density Gr./CC. ASTM-Method D-792 123.55 lbs/ft^3
Water Absorption ASTM-Method D-570 0.0076%
Flame Test ASTM-Method D-635 Self-Extinguishing
2.09 COLOR SELECTION
Laminate Color Selection:
Select from the full range of ONLY Wilsonart®, standard color charts for cabinet faces, exposed ends, open interiors and countertops.
Hinge and Pull Color Selection:
Select from full range of stock and custom colors to coordinate/match: Wilsonart®.
Miscellaneous Hardware Color Selection (support brackets, table frames, rail):
Select from full range of stock and custom colors to coordinate/match: Wilsonart®.
3mm PVC Edge Banding Color Selection:
Select from full range of stock and custom colors to coordinate/match: Wilsonart®."
"""

INPUT_TEXT_8 = """
"PART 2 - PRODUCTS
2.01 SURFACE MATERIAL
A. Cabinet:
1. Exposed fronts shall be faced with vertical grade PF-28 (.028-inch) (.7mm) High
Pressure Laminate (HPL), tested under National Electrical Manufacturers
Association (NEMA) LD3-2005. Decorative laminate shall be thermoset to core
using catalyzed Polyvinyl Acetate (PVA) glue with minimum 80 Pounds per Square
Inch (PSI) pressure and average 180 degree F. temperature. (Lower pressure and
cold curing glues not acceptable.)
2. Panels with exterior PF-28 surfaces shall have Cabinet Liner Surface (CLS) (.020-
inch) (.5mm) interior cabinet liner.
B. Cabinet: Exposed finish ends, modesty panels, and finish backs shall be Thermofused
laminate. Two (2) sided laminate shall become homogenous, thermofused to core face
resulting in a unitized structure. Lamination shall be under precision controlled press
cycle using high pressures of 350-400 PSI and thermosetting temperatures of 380-400
degrees F. Resin impregnated decorative faces shall be thermofused and chemically
cross linked within laminate face and to core structure. Surface texture finishes to be
formed against precision engraved chromed press plates. TF laminates shall be tested
under NEMA LD3-2005 Vertical Grade GP-28 standards. Laminates shall be warranted
for life against delamination.
C. Interior / Drawers: Semi-exposed surfaces laminate shall be homogenous to core face
resulting in panel structure warranted against any delamination. Drawers shall be
laminated and finished in TF laminate.
D. Backs: Shall have a solid color coordinated finish.
E. Open Cabinets: All open cabinets, shelving and etc. Shall have a matching TF laminate
interior to match exterior laminate.
2.02 CORE MATERIALS
A. Particleboard: Shall be high performance industrial grade core. Particleboard shall be
45# - 48# density 3-ply type formation conforming to American National Standards
Institute (ANSI) A208.1 and American Society for Testing and Materials (ASTM)
D1037-91A standards.
B. Medium Density Fiberboard: Core shall be minimum 48# density conforming to ANSI
A208.1 MD-130 standards.
2.03 EDGINGS
A. Door and Drawer Fronts: Edges shall have 3mm radius extrusion banding. 3mm
pattern selection from Stevens 3mm Edge Selector. Fronts shall have radius edges
and corners utilizing automated hot melt adhesive application and trimming.
B. Cabinet Edges: Cabinet sides, top, bottom, adjustable shelves, and other interior
components shall be edged with (.020-inch) flat edge extrusion. Automated hot melt
adhesive application and trimming.
C. Drawer Components: 3/4-inch sides shall be edged with (.020-inch) flat edge extrusion.
Automated hot melt adhesive application and trimming.
D. Selections: Edgebanding to match laminate selections based on Stevens standard
offerings and commercially available stock patterns.
2.04 SELECTIONS AND APPLICATIONS
A. Exposed: Cabinet finish ends, fronts, modesty panels, and finish back laminates shall
be selected from Wilsonart Design Group I patterns.

B. Semi-exposed Surfaces: Selected from Stevens Advantage Pearl- solid color or Maple-
woodgrain pattern.

C. Drawers: Selected from Stevens Pearl- solid color or Maple- woodgrain pattern.
D. Backs: Shall coordinate with interior selection: Pearl- solid color (Pearl interior), Maple
Beige- solid color (Maple woodgrain interior).
E. Laminate Countertops: Selected from Wilsonart Design Group I standard offering.
F. Countertop Supports: Powder coated- three (3) standard colors- Black, Pearl, and
Champagne.
G. Metal Table Frames: Powder coated- three (3) standard colors- Black, Pearl, and
Champagne.
2.05 HARDWARE
A. 5-Knuckle Hinges: Shall be heavy duty 5-knuckle 270 degree pivot reveal overlay style.
Hinges shall have interlaying leaves 270 degree swing constructed of (.090-inch)
thickness steel. Hinges shall be (Grade 1) with hospital ground tips and non-removable
pin. 5-knuckle hinges shall be available in minimum five (5) standard finishes as
detailed in Stevens Advantage Essentials offering. Doors less than 47-inch shall have
two (2) hinges per door. Doors exceeding 47-inch shall have three (3) hinges per door.
5-knuckle hinges shall have vertical adjustment and shall be mounted with two (2)
5mm thread screws each leaf with additional #8 screws: two (2) in cabinet leaf and
three (3) in door leaf. Total nine (9) fasteners per hinge. (Mountings without 5mm
system fasteners not acceptable.)
B. Door Catches: Provide magnetic door catches with opening resistance incompliance
with The Americans with Disabilities Act.
1. Provide one top mounted magnetic catch for base and wall cabinet doors. Provide
two at each tall cabinet door.
C. Pulls: Shall be offered in easy grip 128mm (5-inch size). Pulls shall be available as
selected from Stevens Advantage Bentwire 128 and Contour 128 styles as shown in
Stevens Advantage Essentials offering. Bentwire 128 shall be 8mm diameter wire
formed with powder coated or plated finishes (minimum of three (3) powder coated and
two (2) plated finishes). Contour 128 styles shall be injection molded in high impact
Acetyl Butyl Styrene (ABS) Black, Pearl, or Grey solid colors. (Offerings of less size,
styles, and selection shall not be acceptable.)
D. Drawer Slides: Extension slides shall be bottom and side mount epoxy steel slides.
Lateral stability achieved through a formed captive slide profile. Slides shall glide on
nylon rollers and carry a 100# dynamic load rating. Slides feature both in and out
drawer stop with 3"" self close and adjustable cam side alignment. Slides shall also be
tested under The Scientific Equipment and Furniture Association (SEFA) 6.5 Drawer
Cycle Test.
E. Full Extension Slides (at file drawers only): Full extension ball bearing slides shall be
furnished for all cabinet drawers. Slides shall be side mounted with profile to not
reduce interior drawer space normally provided. Ball bearing slides to be tested under
The Business and Institutional Furniture Manufacturer's Association (BIFMA) X5.5
Section 7. Slides shall pass both 50,000 and 100,000 cycle test with a 120# load
rating.
F. Shelf Supports: Adjustable shelf supports shall be injection molded clear
polycarbonate. Supports shall incorporate integral molded lock tabs to retain shelf from
tipping or inadvertent lift out. Supports shall have 5mm diameter double pin
engagement into precision bored cabinet vertical hole patterns. Adjustment shall be
(32mm) 1 1/4-inch spacings. Supports shall have a compression ridge effecting force
against shelf edge to maintain positive pin engagement. Supports shall have molded-in
screw attachment feature. Static test load shall exceed 200# per clip. Shelf spans
above 27-inch shall have 5-point support with backs drilled to receive a mid-span shelf
support, further reducing deflection. Shelf spans below 27-inch shall have end 4-point
support.
G. Locks: High security 6-tumbler lock system shall be provided where noted by model
number or indicated on drawings. Locks shall have diecast body with dead bolt
engagement tang. (Cylinder locks with attached rotating cams not acceptable.) Locks
shall have removable and interchangeable 6-tumbler core for easy field and customer
re-keying options. Locks shall be master keyed and available key-alike or key-different
with 250 standard key changes and the possibility of up to 2000 total changes on
special order. Each lock provided with a double bit key and face of lock stamped with
key number.
H. Coat Hooks: Under mount and wall mount hooks shall be selected from Stevens
Advantage Gallery Collection designs. Hooks shall be formed cold roll steel with ball
end tips and welded in stamped steel base. Three (3) under mount designs (double,
triple, wardrobe) and three (3) wall mount designs (single, double, schoolhouse). Styles
shall be design coordinated with quality matte nickel plated finish. Attachment with #10
screws.
I. Gromments: Plastic, 3-1/2 inch diameter plastic. Color to be selected.
2.06 COMPONENT DETAILS AND CONSTRUCTION
A. Fronts: Door and drawer fronts shall be 3/4-inch thick. Fronts shall be edged with 3mm
radius edge extrusion with face laminate as described 2.01.A. Automated hot melt
adhesive application and trimming.
B. Wall Cabinets: Components shall be 3/4-inch thick members throughout. Wall cabinet
tops and bottoms shall include back groove and minimum four (4) dowel pins per joint
for insertion into cabinet ends. Wall cabinet ends shall be 3/4-inch thick with back
groove and precision Computer Numerical Control (CNC) drill pattern for accurate
location of fixed members, hardware, and shelf supports. Wall cabinets to have two (2)
integral (dowel into end) mounting frames. (Designs with simple spacer rails or rails
without dowel pin engagement into ends are not acceptable.)
C. Mounting Frames: Incorporated in wall units, tall units, and base units, shall be 3/4-inch
thick with minimum two (2) dowel pins per mounting frame end joint for wall and tall
units. Base units shall have a minimum of three (3) dowel pins per mounting frame end
joint.
D. Tall Cabinets: Components shall be 3/4-inch thick members throughout. Tall cabinet
tops and bottoms shall include back groove and up to eight (8) total dowels per end
joint (based on cabinet depth). Tall cabinet ends shall be 3/4-inch thick with back
groove and precision CNC drill pattern for accurate location of fixed members,
hardware, and shelf supports. Tall cabinets to have two (2) integral (dowel into end)
mounting frames. (Designs with simple spacer rails or rails without dowel pin
engagement into ends are not acceptable.)
E. Base Cabinets: Components shall be 3/4-inch members throughout. Base unit
bottoms shall incorporate back groove and up to eight (8) dowel pins per end joint
(based on cabinet depth). Base units shall have a wide top and back frame feature. A
wide frame in the flat horizontal plane at cabinet front with minimum three (3) dowels
per end joint provides stable squaring of the top area. A second wide frame in the
vertical plane behind back provides stable side-to-side rack resistance. Construction
shall provide lateral and vertical stability. Open rear top area allows for easy wall
mounting and ease of installation of mechanical services. (Sub tops without horizontal
and vertical plane ridged frame members not acceptable.) Base cabinet ends shall be
3/4-inch thick with back groove and precision CNC drill pattern for accurate location of
fixed members, hardware, and shelf supports.
F. Toe Kicks: Bases shall be an integral base design. Construction of end panels, cabinet
bottoms, and horizontal toe kick members are integrally joined together for greater
structural strength. This design facilitates load transfer from upper loaded areas directly
through cabinet end to floor, reducing lower joint stresses. (Separate attached bases
not acceptable.)
G. Cabinet Backs: Shall be in an integrated system of a 1/4-inch prefinished Medium
Density Fiberboard (MDF) back captured in side and horizontal grooves. Unit back to
be further integrated with attachment to 3/4-inch doweled-in mounting frames. Fixed
backs are mechanically fastened into grooves and sealed with hot melt adhesive.
Removable backs shall be set in groove and attached with screws.
H. Adjustable Shelves: All shelves shall be 1-inch thick. Shelving shall have end 4-point
support for spans under 27-inch. Spans above 27-inch shall have 5-point support with
backs drilled to receive additional mid-span shelf support, reducing deflection under
heavier loads.
I. Drawers: Four (4) sided full box design with separate attached front shall be
provided. Drawer members shall be 3/4-inch thick with dowel pin construction at all four
(4) corners. Drawer bottoms shall be 1/4-inch MDF trapped in groove four (4) edges as
well as mechanically fastened. Entire drawer box to be Stevens Advantage TF

laminated. (Drawers utilizing 1/2-inch members or with overlay applied bottoms, non-
captured groove, or staple joint construction not acceptable.)

J. File Drawers: Shall have formed cold roll 16 gauge metal sides. Sides shall be
powder coated and include formed in file hanger rails. Cross bar file hanging adapters
to be provided where legal or special hanging files are specified. File drawers shall be
suspended on full extension ball bearing side mounted slides. Full extension ball
bearing suspensions shall be BIFMA 120# load rated slides. All file drawers including
teachers cabinet shall have a surface mounted pull.
2.07 COUNTERTOPS
A. Plastic Laminate Countertops
1. Countertops shall be high pressure decorative plastic laminate, thermoset to core
using catalyzed PVA glue with minimum average pressure of 80 PSI and average
180 degree F. temperature. Decorative laminate shall meet NEMA LD3-2005
PF-42 (.042-inch) specification standards. Patterns chosen from Wilsonart Design
Grp. I.
2. Laminate tops shall be 1 1/16-inch thick with solid particleboard core structures
and laminated with backer sheet and LS05C: 3mm Polyvinyl Chloride (PVC) edged
countertop with 3mm PVC edged backsplash"
"""

INPUT_TEXT_9 = """
"PART 2 PRODUCTS
2.1 DEFINITIONS
A. Exposed: Includes all surfaces visible when doors and drawers are closed, bottoms of
units where bottom is more than 48 inches above floor, and all visible members,
including shelves in open units or behind clear glass doors.
B. Semi-exposed: Includes all members behind opaque doors, such as shelves, dividers,
interior faces of ends, case backs, drawer sides, back and bottoms, and tops of units
where top is 78 inches or more above floors.
C. Concealed: Includes sleepers, web frames, dust panels and other surfaces not usually
visible after installation.

2.2 MATERIALS: All millwork sizes referred to on the Drawings reflect actual sizes.
A. Plywood:
1. Cabinet - to Receive Plastic Laminate: A-C Grade, fir plywood with
particleboard core.
2. Exposed Stiles for Cabinet Fronts: Minimum 3/4 inch A-C fir plywood, stiles
shall receive plastic laminate.
3. Cabinet Doors - To receive plastic laminate: Shall be 3/4 inch thick, fir plywood
with particleboard core. Exposed cabinet fronts shall receive plastic laminate;
color to be selected by the Architect. Edges of doors shall receive plastic
laminate.
B. Particleboard:

1. Minimum 3/4 inch thick water-resistant particleboard, made with phenol-
formaldehyde resins, complying with ANSI A208.1, Grade M-2:

a. Particleboard Formaldehyde Emissions Level: NPA 8.

C. Cabinets – Shown to Receive Plastic Laminate: Shall be constructed with high density,
high-performance particleboard core with Thermally Fused Melamine, as manufactured
by Flakeboard, or approved equal, and distributed by O’Harco Distributors, Omaha,
Nebraska, or approved equal.
1. All particleboard shall meet or exceed the Commercial Standard CS-236-66,
Federal Specifications, F.S. LLL-B-800A and ASTM D1037-78. Particleboard
shall be 47 pound density with balanced construction and moisture content not to
exceed eight percent (8%).
2. Construct with flush overlay design as follows:
a. All Semi-exposed Areas of Cabinet Construction: Thermally Fused
Melamine prefabricated particleboard. Color shall be as selected by the
Architect.
b. Concealed Areas of Cabinet Construction: Thermally Fused Melamine
prefabricated particleboard. Color shall be as selected by the Architect.
c. Shelves in Cabinets Having Doors: Thermally Fused Melamine
prefabricated particleboard four (4) sides. Color shall be as selected by
the Architect. Provide vinyl edges on all Melamine shelves in cabinets.
d. Cabinet Doors and Drawer Fronts and Edging – to receive Plastic
Laminate: 3/4 inch thick, Thermally Fused Melamine prefabricated
particleboard. Exposed cabinet door and drawer fronts shall receive
plastic laminate. Color shall be as selected by the Architect. Edges shall
be flatedge PVC, color matched to door and drawer fronts.
e. Exposed Stiles (for Cabinet Fronts): Shall be minimum 3/4 inch thick
high density particleboard with Thermally Fused Melamine back surface.
Stiles front and sides shall receive plastic laminate.
f. Drawer, Subfront, Sides and Back: 1/2 inch thick pine or poplar.
(MetaBox 320M as manufactured by Blum, may be substituted at
contractor’s option).
g. Drawer Bottoms: 1/4 inch thick Tempered Masonite.

2.3 CLOSET AND WARDROBE ACCESSORIES
A. Closet Poles: K.V. #770-5 stainless tubing, 1-5/16 inch, or approved equal. Size as
required. Closet pole end caps at each pole, K.V. #766 (two required at each pole).

2.4 CABINET HARDWARE AND ACCESSORIES
A. Cabinet Hinges for Plastic Laminate Casework: Heavy duty, five knuckle, 2-3/4 inch
institutional type hinge, mill ground, hospital tip, tight pin feature with all edges eased.
Hinge to be full wrap around type of tempered steel .095 inch thick. Each hinge to have
minimum nine (9) #7, 5/8 inch FHMS screws to assure positive door attachment. Provide
hinges for cabinet construction specified.
B. Elbow Catches (Install on Left-Hand Leaf on all Pairs of Casework Base Cabinet, Wall
Cabinet, and Tall Cabinet Doors). Spring-loaded catch for pairs of doors with keyed lock
on one side:
a. Product Number 2, as manufactured by Ives Architectural Hardware
Products/Allegion, 11819 North Pennsylvania Street, Carmel, IN 46032
(Tele: 1-877-671-7011).
b. Product Number 245.74.200, as distributed by Hafele America.
C. Magnetic Latches: Stanley SP 41, for single doors and SP 45 for double doors, (US28), or
approved equal. Provide (1) one latch for each base and wall cabinet door and (2) two
latches, one top and bottom, at tall cabinets. www.stanleyhinges.com
D. Cabinet Door and Drawer Keyed Latchbolts: Install at all Cabinet Doors and Drawers,
locations as shown on the Drawings.
a. Olympus Lock Corbin/Russwin Door and Drawer Locks CR1125RD,
with Metal Strikeplate #725-SP-RD; to be furnished and installed by the
Casework Manufacturer.
b. Finish: 26D
c. Install on Right-Hand Leaf on all Pairs of Casework Base Cabinet, Wall
Cabinet, and Tall Cabinet Doors shown to receive locks and all cabinet
drawers shown to receive locks.

E. Drawer Slides at Casework: Side-Mounted, Full-Extension, Steel-Ball-Bearing Drawer
Runners, with 150 pound capacity, equal to Model 4032, as manufactured by Accuride
International, Inc., 7140 Office Circle, Evansville, IN 47715 (Tele: 1-800-626-7096).
Distributor: Hafele America, 1099 Pratt Boulevard, Elk Grove Village, IL 60007 (Tele:
1-800-423-3531).
F. Door and Drawer Pulls for Cabinets: Wire Pulls with 4 inch centers; 1-1/4 inch
projection; Chrome Finish; equal to Product Number 4484-4-US26, as manufactured by
Stanley Hardware, division of The Stanley Works, 6161 East 75th Street, Indianapolis, IN
46250 (Tele: 1-800-346-9445).
1. Acceptable: Product Number 116.07.239, as distributed by Hafele America, 1099
Pratt Boulevard, Elk Grove Village, IL 60007 (Tele: 1-800-423-3531).
G. Door Bumpers (Silencers): Blum, Inc./USA, Product No. FX4041, 1/4 inch diameter, or
Product No. TP 1950.
1. Install minimum of two (2) each Door Bumpers at every swinging Cabinet Door
and Drawer.

H. Chain Stops: Provide on all Base Cabinet, Wall Cabinet, and Tall Cabinet Doors,
adjacent to walls and countertops of greater depth. Field-determine the length and
position of the Chain, for attachment to the Cabinet Box and Door, to prevent the Door
and Door Pull from contacting the adjacent surface.
I. Adjustable Cabinet Shelf Supports: Knape & Vogt (K.V.) Brackets #346 ANO, or
approved equal. Space holes for brackets at 1 inch on center.
J. Door Bumpers: Blum FX4041, 1/4” dia. x 1.5, or approved equal.

K. Power and Computer Cable Grommets: Work Surface-Mounted, Black Plastic “Flip-
Top” Grommets for 2-1/2 inch diameter hole, with 2-1/4 inch inside diameter; Model

Number EDP Flip-Top as manufactured by Doug Mockett and Company, Inc., 1915
Abalone Avenue, Torrance, CA 90501 (Tele: 1-800-523-1269).
L. Totes (Art Room B186):
1. Replacement Tote Tray by Diversified Woodcrafts or Sherley K’s.
a. Heavy Duty Plastic Tote Trays
b. 19” Long x 10 1/2” Wide x 3 1/2” High (Verify Totes dimensions to work
with the case work dimension. Refer to the drawings elevation 2/A7.4)
c. Color: Gray
d. Quantity: 96 minimum (48 totes per 36 inch wide cabinet)
M. Wardrobe Rod: To be 1-1/16 inch round rod, LH-362, supported by LH-363 flanges.
N. Wardrobe Mirror: For each wardrobe cabinet provide one of the following:
1. Two 10 inch wide by 12 inch high mirrors for wheelchair and ambulatory
persons. One mounted at 35 inches above finish floor to bottom of reflecting
surface per ADA standards, and one mounted at 72 inches to top.
2. One 10 inch wide by 38 inch high mirror mounted at 35 inches above finish floor
to bottom of reflecting surface per ADA Standards.
3. Mirrors shall be framed mirrors similar to American Specialties, Inc. 101-14
Framed Mirror - #8 Mirror Polished Stainless Steel, or similar.

O. Administrative Mailboxes:
1. Support Panels: Sherley K’s
a. Uniform Rib Style #P1029
b. Color: “White”
c. Nine (9.5) sets of panels (27 panels) 48 inches tall.
2. Name Plate Cover: Shall be Clear Plastic Edge Molding
a. Size: As required to fit over the front edge of the shelfs
b. Provide edge molding on each movable mailbox shelf and a few spares
for maintenance. Provide a minimum of 120 to run the full length of the
shelf.

2.5 SOLID SURFACE – (SS-1) COUNTERTOPS & CLASSROOM LOCKER CAP
A. Solid Surface shall be Corian® Solid Surface, shall be as manufactured by DuPont
Corian, Chestnut Run Plaza, Wilmington, DE, 19880 (Tele: 1-800-426-7426), or
approved equal. Substitutions: Section 01 60 00 - Product Requirements. Work shall be
performed by a fabricator/installer certified by the Solid Surface Manufacturer.
1. Color shall be as selected by the Owner and Architect.
2. Applicable Standards:
a. NEMA Publications No. LD-3-1980.
b. NSF Compliance - National Sanitation Foundation, NSF Standard #51.
c. ANSI Z124.3, various performance tests for plastic lavatories.
d. ASTM D638, physical tests for sheet materials.
e. ASTM E-84, test methods for determining flammability of materials.
3. Material: Shall be minimum 3/4 inch thick, fabricated as shown and dimensioned
on the Drawings.
4. Form countertops with the “No-Drip” edge as shown on the drawings.
5. Form countertops with the integral backsplash as shown on the drawings.
6. Sealant - used in conjunction with solid surface: Shall be Type SCS-1752,
supplied by Manufacturer’s distributor. Sealant shall be sanded (and colored as
required) to match installed solid surface.
7. Warranty: Provide ten (10) year installed warranty guaranteeing product quality
of Corian, including fabrication and installation.
B. The following solid surface products are acceptable:
1. Formica Solid Surface, as manufactured by Formica Corporation/The Diller
Corporation, 10155 Reading Road, Cincinnati, oh 45241 (Tele: 1-800-367-6422).

2.6 SOLID SURFACE – WINDOW STOOLS/SILLS (SS-2)
A. Solid Surface shall be Corian® Solid Surface, ""Willow"" as manufactured by DuPont
Corian, Chestnut Run Plaza, Wilmington, DE, 19880 (Tele: 1-800-426-7426), or
approved equal. Substitutions: Section 01 60 00 - Product Requirements. Work shall be
performed by a fabricator/installer certified by the Solid Surface Manufacturer.
1. Applicable Standards:
a. NEMA Publications No. LD-3-1980.
b. NSF Compliance - National Sanitation Foundation, NSF Standard #51.
c. ANSI Z124.3, various performance tests for plastic lavatories.
d. ASTM D638, physical tests for sheet materials.
e. ASTM E-84, test methods for determining flammability of materials.
2. Material: Shall be minimum 1/2 inch thick, fabricated as shown and dimensioned
on the Drawings.
3. Sealant - used in conjunction with solid surface: Shall be Type SCS-1752,
supplied by Manufacturer’s distributor. Sealant shall be sanded (and colored as
required) to match installed solid surface.
4. Warranty: Provide ten (10) year installed warranty guaranteeing product quality
of Corian, including fabrication and installation.
B. The following solid surface products are acceptable:
1. Formica Solid Surface, “Gray Renew” #749 as manufactured by Formica
Corporation/The Diller Corporation, 10155 Reading Road, Cincinnati, oh 45241
(Tele: 1-800-367-6422).
2. Wilsonart Solid Surface, “Tumbled Stone” #9220CE as manufactured by
Wilsonart Engineered Surfaces/Wilsonart Americas, A2501 Wilsonart Drive,
Temple, TX 76504 (Tele: 1-800-433-3222).

2.7 PLASTIC LAMINATE
A. All plastic laminate countertops shall have a radius edge except for those located in
rooms with counter mounted sinks. Where counter mounted sinks are installed, those
plastic laminate countertops shall be no drip.
B. Standard Plastic Laminate shall be products as manufactured by Wilsonart of the
specified colors/patterns.
1. For countertops and edges - shown post-formed: General Purpose Forming Grade
12/HGP, nominal thickness: .042 inch, high-pressure plastic laminate, matte
finish. Color and finish shall be selected by the Architect.
2. Backing sheets: .020 inch thick, Type V, Grade 91, plastic laminate.
3. Core material for plastic laminate cabinet and countertop construction: Minimum
3/4 inch thick water resistant particleboard, made with phenol-formaldehyde
resins, complying with ANSI A208.1, Grade M-2:
a. Particleboard Formaldehyde Emissions Level: NPA 8.
4. Adhesives for plastic laminates: Formica #100 Non-Flammable Brushable
Contact Adhesive, or Formica #140 Brushable Contact Adhesive. Sand back of
sheets for bonding adhesive.
5. Color Selections shall be determined once the school has been named and
school colors selected by the Owner.
a. PL-1: To Be Determined
b. PL-2: To Be Determined
c. PL-3: To Be Determined

2.8 FASTENINGS
A. Nails - for interior finish carpentry materials shall be as follows:
1. Stock up to 1/2"" thick - 4d finishing or casing nails.
2. Stock 1/2"" to 3/4"" thick - 6d finishing or casing nails.
3. Stock 3/4"" to 1"" thick - 8d finishing or casing nails.
4. Stock 1"" to 1-1/2"" thick -10d finishing or casing nails.
B. Miscellaneous Fastenings: Screws, toggle bolts, expansion bolts and other miscellaneous
fastenings to secure finish carpentry items in place.

2.9 CONSTRUCTION OF NON-FABRICATED ITEMS:
A. Perform all work as a minimum to AWI Premium Grade Standards.
1. Factory assemble all parts to largest extent possible. Items too large for entrance
into area may be made into attachable sections. Fabricate each section complete
in itself with provisions for job connection. Fabricate with flush type fronts
overlapping ends. Finish panel edges to match exterior surfaces. Assemble body
panel joints without use of exposed fasteners.
2. Perform assembly with nickel plated hardware applied in such a manner that a
section can be replaced by disengaging hardware and removing screws from back
of cabinet or assembling can be done by fabricating parts to accurate fit and
assembling with appropriate joinery and adhesives to result in true, level and
plumb units.
3. Scribe all tops and backsplashes to walls and adjoining surfaces. Make all
countertops and backsplashes of plastic laminate unless otherwise indicated.
(Seal around backsplashes with clear sealant.)
4. Provide cutouts and access panels when installed work covers mechanical or
electrical items requiring access.
B. Install bumpers on all cabinet drawers and doors.
C. Fabricate base cabinet ends and dividers of plywood with corner joints between frame
members fully lock jointed, glued and screwed.
D. Dado and glue cabinet backs into sides and bottom.
E. Dado drawer bottoms into sides and front, glue and nail. Blind dovetail sides into fronts
and glue. Slightly round top edges of sides.
F. Dado drawer rails into dividers and ends. Glue and nail.
G. Secure countertops to cabinets from underside using screws of length to avoid damaging
top.
H. Finish all Melamine finished shelves in cabinets with vinyl edges.

2.10 FABRICATION
A. Shop assemble casework for delivery to site in units easily handled and to permit passage
through building openings.
B. When necessary to cut and fit on site, fabricate materials with ample allowance for
cutting. Furnish trim for scribing and site cutting.
C. Apply high pressure decorative laminate finish in full uninterrupted sheets consistent
with manufactured sizes. Fit corners and joints hairline; secure with concealed fasteners.
Locate counter butt joints minimum 2 feet from sink cut-outs.
D. Mechanically fasten back splash to counter tops with steel brackets at 16 inches on
center.
E. Fabricate cabinets and counter tops with cutouts for required items to be set into work.
Verify locations of cutouts from on-site dimensions. Seal cut edges.
"
"""