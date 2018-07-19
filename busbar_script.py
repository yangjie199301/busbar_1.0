from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

args = []
with open('d:\py_test\data.txt','r') as f:
    for line in f.readlines():
        line = line.strip()
        args.append(line)

#args = ['180','60','4','60','108000000000.0','193000000000.0','0.34','0.31','0.399','0.0485',
#'59700.0','1390.0','25','','100','5','1','M4',(0,0)]
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=330,height=188)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
session.viewports['Viewport: 1'].setValues(displayedObject=None)

executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
Mdb()

def create_busbar(contact_length,width,depth,radius,n=1,center=((0.0,0.0))):
	##Create Busbar
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=STANDALONE)
	s.rectangle(point1=(-contact_length/2, -width/2), point2=(contact_length/2, width/2))
	#Get Number Of Hole
	while n >0:
		s.CircleByCenterPerimeter(center=center[n-1], point1=(center[n-1][0],center[n-1][1]-float(radius)))
		n -= 1
	p = mdb.models['Model-1'].Part(name='Busbar', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Busbar']
	p.BaseSolidExtrude(sketch=s, depth=depth)
	s.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']
	#Mesh Busbar
	p = mdb.models['Model-1'].parts['Busbar']
	p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
	elemType1 = mesh.ElemType(elemCode=DC3D8E, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=DC3D6E, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=DC3D4E, elemLibrary=STANDARD)
	p = mdb.models['Model-1'].parts['Busbar']
	c = p.cells
	cells = c[0:1]
	pickedRegions =(cells, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
	p = mdb.models['Model-1'].parts['Busbar']
	p.generateMesh()

def create_busbar_side(length,width,depth,contact):
	#
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=STANDALONE)
	s.rectangle(point1=(0.0, -width/2), point2=(length-contact, width/2))
	p = mdb.models['Model-1'].Part(name='Busbar_side', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Busbar_side']
	p.BaseSolidExtrude(sketch=s, depth=depth)
	s.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']
	#Mesh Busbar_side
	p = mdb.models['Model-1'].parts['Busbar_side']
	p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
	elemType1 = mesh.ElemType(elemCode=DC3D8E, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=DC3D6E, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=DC3D4E, elemLibrary=STANDARD)
	p = mdb.models['Model-1'].parts['Busbar_side']
	c = p.cells
	cells = c[0:1]
	pickedRegions =(cells, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
	p = mdb.models['Model-1'].parts['Busbar_side']
	p.generateMesh()

def create_nut(radius1,radius2,depth):
	#Create Nut
	s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=STANDALONE)
	s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius1))
	s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius2))
	p = mdb.models['Model-1'].Part(name='Nut', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Nut']
	p.BaseSolidExtrude(sketch=s1, depth=depth)
	s1.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts['Nut']
	del mdb.models['Model-1'].sketches['__profile__']

	#Mesh Nut
	p = mdb.models['Model-1'].parts['Nut']
	p.seedPart(size=0.6, deviationFactor=0.1, minSizeFactor=0.1)
	elemType1 = mesh.ElemType(elemCode=DC3D8E, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=DC3D6E, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=DC3D4E, elemLibrary=STANDARD)
	p = mdb.models['Model-1'].parts['Nut']
	c = p.cells
	cells = c[0:1]
	pickedRegions =(cells, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
	p = mdb.models['Model-1'].parts['Nut']
	p.generateMesh()



def create_bolt(radius1,depth1,radius2,depth2):
	#Create Bolt
	s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=STANDALONE)
	s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius1))
	p = mdb.models['Model-1'].Part(name='Bolt', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Bolt']
	p.BaseSolidExtrude(sketch=s1, depth=depth1)
	s1.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts['Bolt']
	del mdb.models['Model-1'].sketches['__profile__']
	p = mdb.models['Model-1'].parts['Bolt']
	f, e = p.faces, p.edges
	t = p.MakeSketchTransform(sketchPlane=f[1], sketchUpEdge=e[0], sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, depth1))
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=17.85, gridSpacing=0.44, transform=t)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models['Model-1'].parts['Bolt']
	p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
	s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius2))
	p = mdb.models['Model-1'].parts['Bolt']
	f1, e1 = p.faces, p.edges
	p.SolidExtrude(sketchPlane=f1[1], sketchUpEdge=e1[0], sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, sketch=s, depth=depth2, flipExtrudeDirection=OFF)
	s.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']

	#Mesh Bolt
	p = mdb.models['Model-1'].parts['Bolt']
	c = p.cells
	pickedRegions = c[0:1]
	p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
	elemType1 = mesh.ElemType(elemCode=DC3D8E, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=DC3D6E, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=DC3D4E, elemLibrary=STANDARD)
	cells = c[0:1]
	pickedRegions =(cells, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
	p.seedPart(size=1.1, deviationFactor=0.1, minSizeFactor=0.1)
	p.generateMesh()



def create_gasket(radius1,radius2,depth):
	#Create Gasket
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=STANDALONE)
	s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius1))
	s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius2))
	p = mdb.models['Model-1'].Part(name='Gasket', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Gasket']
	p.BaseSolidExtrude(sketch=s, depth=depth)
	s.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts['Gasket']
	del mdb.models['Model-1'].sketches['__profile__']

	#Mesh Gasket
	p = mdb.models['Model-1'].parts['Gasket']
	p.seedPart(size=0.6, deviationFactor=0.1, minSizeFactor=0.1)
	elemType1 = mesh.ElemType(elemCode=DC3D8E, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=DC3D6E, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=DC3D4E, elemLibrary=STANDARD)
	p = mdb.models['Model-1'].parts['Gasket']
	c = p.cells
	cells = c[0:1]
	pickedRegions =(cells, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
	p = mdb.models['Model-1'].parts['Gasket']
	p.generateMesh()


def set_material(elastic1,elastic2,conductivity1,conductivity2,e_conductivity1,e_conductivity2):
	#elastic1_tuple;elastic2_tuple;other_float
	#Set Up Materials of Copper And Steel
	mdb.models['Model-1'].Material(name='Copper')
	mdb.models['Model-1'].materials['Copper'].Elastic(table=(elastic1, ))
	mdb.models['Model-1'].materials['Copper'].Conductivity(table=((conductivity1, ), ))
	mdb.models['Model-1'].materials['Copper'].JouleHeatFraction()
	mdb.models['Model-1'].materials['Copper'].ElectricalConductivity(table=((e_conductivity1, ), ))
	mdb.models['Model-1'].Material(name='Steel')
	mdb.models['Model-1'].materials['Steel'].Elastic(table=(elastic2, ))
	mdb.models['Model-1'].materials['Steel'].Conductivity(table=((conductivity2, ), ))
	mdb.models['Model-1'].materials['Steel'].JouleHeatFraction()
	mdb.models['Model-1'].materials['Steel'].ElectricalConductivity(table=((e_conductivity2, ), ))
	#Create Section
	mdb.models['Model-1'].HomogeneousSolidSection(name='Section-Copper', material='Copper', thickness=None)
	mdb.models['Model-1'].HomogeneousSolidSection(name='Section-Steel', material='Steel', thickness=None)
	#Assign Section
	#Busbar Section-Copper
	p = mdb.models['Model-1'].parts['Busbar']
	c = p.cells
	cells = c[0:1]
	region = p.Set(cells=cells, name='Set-Busbar')
	p = mdb.models['Model-1'].parts['Busbar']
	p.SectionAssignment(region=region, sectionName='Section-Copper', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

	p = mdb.models['Model-1'].parts['Busbar_side']
	c = p.cells
	cells = c[0:1]
	region = p.Set(cells=cells, name='Set-Busbar_side')
	p = mdb.models['Model-1'].parts['Busbar_side']
	p.SectionAssignment(region=region, sectionName='Section-Copper', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
	#Bolt Section-Steel
	p = mdb.models['Model-1'].parts['Bolt']
	c = p.cells
	cells = c[0:1]
	region = p.Set(cells=cells, name='Set-Bolt')
	p = mdb.models['Model-1'].parts['Bolt']
	p.SectionAssignment(region=region, sectionName='Section-Steel', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
	p = mdb.models['Model-1'].parts['Gasket']
	c = p.cells
	cells = c[0:1]
	region = p.Set(cells=cells, name='Set-Gasket')
	p = mdb.models['Model-1'].parts['Gasket']
	p.SectionAssignment(region=region, sectionName='Section-Steel', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

	p = mdb.models['Model-1'].parts['Nut']
	c = p.cells
	cells = c[0:1]
	region = p.Set(cells=cells, name='Set-Nut')
	p = mdb.models['Model-1'].parts['Nut']
	p.SectionAssignment(region=region, sectionName='Section-Steel', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
######
def assembly(d_bolt,d_gasket,d_busbar,n,center,contact,length):
	a = mdb.models['Model-1'].rootAssembly
	a.DatumCsysByDefault(CARTESIAN)
	p = mdb.models['Model-1'].parts['Busbar']
	a.Instance(name='Busbar-1', part=p, dependent=ON)
	a.Instance(name='Busbar-2', part=p, dependent=ON)
	a.translate(instanceList=('Busbar-2', ), vector=(0.0, 0.0, d_bolt+d_gasket+d_busbar))
	#: The instance Busbar-2 was translated by 0., 0., 7.6
	a.translate(instanceList=('Busbar-1', ), vector=(0.0, 0.0, d_bolt+d_gasket))
	#: The instance Busbar-1 was translated by 0., 0., 3.6
	p = mdb.models['Model-1'].parts['Busbar_side']
	a.Instance(name='Busbar_side-1', part=p, dependent=ON)
	a.Instance(name='Busbar_side-2', part=p, dependent=ON)
	a.translate(instanceList=('Busbar_side-1', ), vector=(contact/2, 0.0, d_bolt+d_gasket))
	a.translate(instanceList=('Busbar_side-2', ), vector=(-(length-contact/2), 0.0,d_bolt+d_gasket+d_busbar))

	for i in range(1,n+1):
		p = mdb.models['Model-1'].parts['Bolt']
		a.Instance(name='Bolt-'+str(i), part=p, dependent=ON)
		p = mdb.models['Model-1'].parts['Gasket']
		a.Instance(name='Gasket-'+str(i), part=p, dependent=ON)
		p = mdb.models['Model-1'].parts['Nut']
		a.Instance(name='Nut-'+str(i), part=p, dependent=ON)

		a.translate(instanceList=('Gasket-'+str(i), ), vector=(0.0,0.0, d_bolt))
		#: The instance Gasket-1 was translated by 0., 0., 2.8
		a.translate(instanceList=('Nut-'+str(i), ), vector=(0.0,0.0, d_bolt+d_gasket+d_busbar*2))
		# The instance Nut-1 was translated by 0., 0., 11.6
		a.translate(instanceList=('Bolt-'+str(i), ), vector=(center[i-1][0],center[i-1][1],0.0))
		a.translate(instanceList=('Gasket-'+str(i), ), vector=(center[i-1][0],center[i-1][1],0.0))
		a.translate(instanceList=('Nut-'+str(i), ), vector=(center[i-1][0],center[i-1][1],0.0))
def contact(n):
	region = []
	#busbar1 and busbar2
	a = mdb.models['Model-1'].rootAssembly
	s1 = a.instances['Busbar-2'].faces
	#side1Faces1 = s1[-1:-2]
	a.Surface(side1Faces=s1[-1:], name='CP-Busbar-2')
	region.append(a.surfaces['CP-Busbar-2'])
	s1 = a.instances['Busbar-1'].faces
	#side1Faces1 = s1[-2]
	a.Surface(side1Faces=s1[-2:-1], name='CP-Busbar-1')
	region.append(a.surfaces['CP-Busbar-1'])
	mdb.models['Model-1'].Tie(name='CP-Busbar-2-Busbar-1', master=region[-2],slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)


	s1 = a.instances['Busbar-1'].faces
	side1Faces1 = s1[2:3]
	a.Surface(side1Faces=side1Faces1, name='CP-3-Busbar-1')
	region1=a.surfaces['CP-3-Busbar-1']
	s1 = a.instances['Busbar_side-1'].faces
	side1Faces1 = s1[0:1]
	a.Surface(side1Faces=side1Faces1, name='CP-2-Busbar_side-1')
	region2=a.surfaces['CP-2-Busbar_side-1']
	s1 = a.instances['Busbar-2'].faces
	side1Faces1 = s1[0:1]
	a.Surface(side1Faces=side1Faces1, name='CP-9-Busbar-2')
	region3=a.surfaces['CP-9-Busbar-2']
	a = mdb.models['Model-1'].rootAssembly
	s1 = a.instances['Busbar_side-2'].faces
	side1Faces1 = s1[2:3]
	a.Surface(side1Faces=side1Faces1, name='CP-9-Busbar_side-2')
	region4=a.surfaces['CP-9-Busbar_side-2']
	mdb.models['Model-1'].Tie(name='CP-1-Busbar-1-Busbar_side-1', master=region1,
	slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
	mdb.models['Model-1'].Tie(name='CP-2-Busbar-2-Busbar_side-2', master=region3,
	slave=region4, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

	#
	for i in range(1,n+1):
		# NO.1
		s1 = a.instances['Bolt-'+str(i)].faces
		side1Faces1 = s1[3:4]
		a.Surface(side1Faces=side1Faces1, name='CP-1-Bolt-'+str(i))
		region.append(a.surfaces['CP-1-Bolt-'+str(i)])

		s1 = a.instances['Gasket-'+str(i)].faces
		side1Faces1 = s1[3:4]
		a.Surface(side1Faces=side1Faces1, name='CP-1-Gasket-'+str(i))
		region.append(a.surfaces['CP-1-Gasket-'+str(i)])
		mdb.models['Model-1'].Tie(name='CP-1-Bolt-'+str(i)+'-Gasket-'+str(i), master=region[-2], slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

		#NO.2
		s1 = a.instances['Busbar-1'].faces
		#side1Faces1 = s1[-1]
		a.Surface(side1Faces=s1[-1:], name='CP-2-Busbar-1')
		region.append(a.surfaces['CP-2-Busbar-1'])
		s1 = a.instances['Gasket-'+str(i)].faces
		#side1Faces1 = s1[2:3]
		a.Surface(side1Faces=s1[2:3], name='CP-2-Gasket-'+str(i))
		region.append(a.surfaces['CP-2-Gasket-'+str(i)])
		mdb.models['Model-1'].Tie(name='CP-2-Busbar-1-Gasket-'+str(i), master=region[-2], slave=region[-1],positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

		#NO.3
		s1 = a.instances['Busbar-1'].faces
		#side1Faces1 = s1[-2-i]
		a.Surface(side1Faces=s1[-2-i:-2-i+1], name='CP-3-Busbar-1-'+str(i))
		region.append(a.surfaces['CP-3-Busbar-1-'+str(i)])
		s1 = a.instances['Bolt-'+str(i)].faces
		#side1Faces1 = s1[0:1]
		a.Surface(side1Faces=s1[0:1], name='CP-3-Bolt-'+str(i))
		region.append(a.surfaces['CP-3-Bolt-'+str(i)])
		mdb.models['Model-1'].Tie(name='CP-3-Busbar-1'+'-Bolt-'+str(i), master=region[-2], slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

		#NO.4
		s1 = a.instances['Busbar-2'].faces
		a.Surface(side1Faces=s1[-2-i:-2-i+1], name='CP-4-Busbar-2-'+str(i))
		region.append(a.surfaces['CP-4-Busbar-2-'+str(i)])

		s1 = a.instances['Bolt-'+str(i)].faces
		#side1Faces1 = s1[0:1]
		a.Surface(side1Faces=s1[0:1], name='CP-4-Bolt-'+str(i))
		region.append(a.surfaces['CP-4-Bolt-'+str(i)])

		mdb.models['Model-1'].Tie(name='CP-4-Busbar-2-Bolt-'+str(i), master=region[-2], slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
		#NO.5
		s1 = a.instances['Busbar-2'].faces
		side1Faces1 = s1[-2-i:-2-i+1]
		a.Surface(side1Faces=side1Faces1, name='CP-5-Busbar-2-'+str(i))
		region.append(a.surfaces['CP-5-Busbar-2-'+str(i)])

		s1 = a.instances['Nut-'+str(i)].faces
		side1Faces1 = s1[3:4]
		a.Surface(side1Faces=side1Faces1, name='CP-5-Nut-'+str(i))
		region.append(a.surfaces['CP-5-Nut-'+str(i)])

		mdb.models['Model-1'].Tie(name='CP-5-Busbar-2-Nut-'+str(i), master=region[-2], slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
		#NO.6
		s1 = a.instances['Bolt-'+str(i)].faces
		side1Faces1 = s1[0:1]
		a.Surface(side1Faces=side1Faces1, name='CP-6-Bolt-'+str(i))
		region.append(a.surfaces['CP-6-Bolt-'+str(i)])

		s1 = a.instances['Nut-'+str(i)].faces
		side1Faces1 = s1[1:2]
		a.Surface(side1Faces=side1Faces1, name='CP-6-Nut-'+str(i))
		region.append(a.surfaces['CP-6-Nut-'+str(i)])

		mdb.models['Model-1'].Tie(name='CP-6-Bolt-'+str(i)+'-Nut-'+str(i), master=region[-2], slave=region[-1], positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

def set_define(n):
	#set_film
	a = mdb.models['Model-1'].rootAssembly
	f1 = a.instances['Busbar_side-1'].faces
	faces1 = f1[1:6]
	f2 = a.instances['Busbar_side-2'].faces
	faces2 = f2[0:2]+f2[3:6]
	f3 = a.instances['Busbar-1'].faces
	faces3 = f3[0:2]+f3[3:4]+f3[-1:]
	f4 = a.instances['Busbar-2'].faces
	faces4 = f4[1:4]+f4[-2:-1]
	temp = faces1 + faces2 +faces3 + faces4
	for i in range(1,n+1):
		f1 = a.instances['Bolt-'+str(i)].faces
		faces1 = f1[1:3]+f1[4:5]
		f2 = a.instances['Gasket-'+str(i)].faces
		faces2 = f2[0:1]+f2[3:4]
		f3 = a.instances['Nut-'+str(i)].faces
		faces3 = f3[0:1]+f3[2:3]
		temp = temp + faces1 + faces2 +faces3
	a.Surface(side1Faces=temp, name='Surf-film')
	#set_current &set_voltage
	a = mdb.models['Model-1'].rootAssembly
	f1 = a.instances['Busbar_side-1'].faces
	faces1 = f1[2:3]
	a.Surface(side1Faces=faces1, name='Surf-current')
	f1 = a.instances['Busbar_side-2'].faces
	faces1 = f1[0:1]
	a.Set(faces=faces1, name='Set-voltage')
	#set_heat
	a = mdb.models['Model-1'].rootAssembly
	f1 = a.instances['Busbar-1'].faces
	faces1 = f1[6:7]
	a.Surface(side1Faces=faces1, name='Surf-heat')

def step_load(current,width,depth,temperature,q):
	a = mdb.models['Model-1'].rootAssembly
	mdb.models['Model-1'].CoupledThermalElectricStep(name='Step-1', previous='Initial', response=STEADY_STATE, amplitude=RAMP)
	mdb.models['Model-1'].FilmConditionProp(name='IntProp-1', temperatureDependency=OFF, dependencies=0, property=((5e-06, ), ))
	region1=a.surfaces['Surf-film']
	mdb.models['Model-1'].FilmCondition(name='Int-1', createStepName='Step-1',
	surface=region1, definition=PROPERTY_REF, interactionProperty='IntProp-1',
	sinkTemperature=temperature, sinkAmplitude='', sinkDistributionType=UNIFORM, sinkFieldName='')

	region2 = a.surfaces['Surf-current']
	#face_current = current/width/depth
	mdb.models['Model-1'].SurfaceCurrent(name='Load-Current', createStepName='Step-1', region=region2, magnitude=0.02777777777777778*2)

	region3 = a.surfaces['Surf-heat']
	s = a.instances['Busbar-1'].faces[-1].getSize()
	face_heat = q/s
	mdb.models['Model-1'].SurfaceHeatFlux(name='Load-heat', createStepName='Step-1', region=region3, magnitude=face_heat)

	region4 = a.sets['Set-voltage']
	mdb.models['Model-1'].ElectricPotentialBC(name='BC-Voltage', createStepName='Initial', region=region4, distributionType=UNIFORM, fieldName='', magnitude=0.0)

	stack = []
	for i in a.instances.keys():
		cells = a.instances[i].cells
		tmp = cells[0:1]
		stack.append(tmp)
	region5 = a.Set(cells=stack, name='Set-toltal')
	mdb.models['Model-1'].Temperature(name='Predefined Field-1',
	createStepName='Initial', region=region5, distributionType=UNIFORM, crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(temperature, ))



def job():
	mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
	mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

def main():
	bolt_type ={'M4':(3.5,2.8,2,14,3.5,2,3.2,4.5,2.15,0.8),'M5':(4,3.4,2.5,16,4,2.5,4,5,2.9,1),'M6':(5,4,3,18,5,3,5,6,3.2,1.6),'M8':(6.5,5.3,4,20,6.5,4,6,8,4.5,1.6)}
	tmp= bolt_type[(args[-2])]
	#circle_position
	#center = [(0.0,0.0)]
	#center = [(-15,0.0),(0.0,15),(0.0,-15)]
	if int(args[-3]) == 1:
		center = [eval(args[-1])]
	else:
		center = eval(args[-1])
	bolt_ag = tmp[:4]
	nut_ag = tmp[4:7]
	gasket_ag = tmp[7:]

	#create_bolt(radius1,depth1,radius2,depth2)
	create_bolt(bolt_ag[0],bolt_ag[1],bolt_ag[2],bolt_ag[3])

	#create_nut(radius1,radius2,depth)
	create_nut(nut_ag[0],nut_ag[1],nut_ag[2])

	#create_gasket(radius1,radius2,depth)
	create_gasket(gasket_ag[0],gasket_ag[1],gasket_ag[2])

	#create_busbar(contact_length,width,depth,radius,n=1,center=(0.0,0.0))
	create_busbar(int(args[3]),int(args[1]),int(args[2]),bolt_ag[2],n=int(args[-3]),center=center)

	#create_busbar_side(length,width,depth,contact)
	create_busbar_side(int(args[0]),int(args[1]),int(args[2]),int(args[3]))

	#set_material(elastic1,elastic2,conductivity1,conductivity2,e_conductivity1,e_conductivity2)
	set_material((float(args[4]),float(args[6])),(float(args[5]),float(args[7])),float(args[8]),float(args[9]),float(args[10]),float(args[11]))

	#assembly(d_bolt,d_gasket,d_busbar,n,center,contact,length)
	assembly(tmp[1],tmp[-1],float(args[2]),int(args[-3]),center,float(args[3]),float(args[0]))

	#contact(n)
	contact(int(args[-3]))
	#set_define(n)
	set_define(int(args[-3]))
	#step_load(current,width,depth,temperature,q)
	step_load(float(args[-5]),float(args[1]),float(args[2]),int(args[-7]),1)
	job()


main()
