import numpy as np
import geo_dis_parse as gdp

def getdis(input_file):
  with open(input_file) as file:
      data = file.readlines()
      for i in range(len(data)):
          head = data[i].split(' ')
          if head[0]=="EDGE_WEIGHT_TYPE:":
              Dformat = head[1]
          if head[0]=="DIMENSION:":
              Di = int(head[1])
          if data[i]=="NODE_COORD_SECTION\n":
              space=i
              break

      if Dformat=="EUC_2D\n":
          value=np.zeros((Di,Di))
          for i in range(Di):
              line=data[1+space+i].split(' ')
              for j in range(Di):
                  line0=data[1+space+j].split(' ')
                  value[i][j]=np.sqrt((float(line[1])-float(line0[1]))**2+(float(line[2])-float(line0[2]))**2)
      else:
          value = np.zeros((Di, Di))
          GtU=np.zeros((Di,2))
          for i in range(Di):
              line=data[1+space+i].split(' ')
              GtU[i,0]=float(line[2])
              GtU[i,1]=float(line[3])
          value=gdp.geo_data_parse(GtU)
      for i in range(len(value)):
          value[i][i]=float('inf')
  return value

##value is a matrix saving the distance of each pair of nodes
