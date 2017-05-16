# -*- coding: utf-8 -*-
#
#Auto-Rigger v1.9 for biped models

#Created: june 5  2015
#BY http://steamcommunity.com/id/OMGTheresABearInMyOatmeal/
#feel free to modify the script for your own use
#find any bugs or suggestions message me in the workshop page comments

from PySide import QtCore, QtGui
import vs, os,ast, sys
#get model name and store file name
animSet = sfm.GetCurrentAnimationSet()
gameModel = animSet.gameModel

name="rig_"+(animSet.GetName())[:-1]+".py"
#str(gameModel)[b+1:e]
#print(gameModel.GetName())
bonelist=[]
fingerbones={}


class Ui_window(QtGui.QMainWindow):




    
    def hide(self):
        if  self.sp1.isChecked():
            self.label_6.setEnabled(False)
            self.label_7.setEnabled(False)
            self.label_8.setEnabled(False)
            self.bone_spine2.setEnabled(False)
            self.bone_spine3.setEnabled(False)
            self.bone_spine1.setEnabled(False)
        
        if  self.sp2.isChecked():
            self.label_6.setEnabled(True)
            self.bone_spine1.setEnabled(True)
            self.label_7.setEnabled(False)
            self.label_8.setEnabled(False)
            self.bone_spine2.setEnabled(False)
            self.bone_spine3.setEnabled(False)

        if  self.sp3.isChecked():
            self.label_7.setEnabled(True)
            self.bone_spine2.setEnabled(True)
            self.bone_spine3.setEnabled(False)
            self.label_8.setEnabled(False)

        if  self.sp4.isChecked():
            self.label_7.setEnabled(True)
            self.bone_spine2.setEnabled(True)
            self.bone_spine3.setEnabled(True)
            self.label_8.setEnabled(True)

        if self.toeoption.isChecked():

            self.footroll_checkbox.setEnabled(True)
            self.bone_toeL.setEnabled(True)
            self.bone_toeR.setEnabled(True)
            self.label_12.setEnabled(True)
            self.label_17.setEnabled(True)
        else:
            self.footroll_checkbox.setEnabled(False)
            self.footroll_checkbox.setChecked(False)
            
        if self.shoulderoption.isChecked():
            self.bone_collarR.setEnabled(True)
            self.bone_collarL.setEnabled(True)
            self.label_19.setEnabled(True)
            self.label_15.setEnabled(True)

        if self.shoulderoption.isChecked()==False:
            self.bone_collarR.setEnabled(False)
            self.bone_collarL.setEnabled(False)
            self.label_19.setEnabled(False)
            self.label_15.setEnabled(False)

            
        if self.toeoption.isChecked()==False:
            self.bone_toeL.setEnabled(False)
            self.bone_toeR.setEnabled(False)
            self.label_12.setEnabled(False)
            self.label_17.setEnabled(False)

    def opensave(self):      ##opens rig file to reselect bones
        
        filename=None
        try:
            
            filename, foo = QtGui.QFileDialog.getOpenFileName(None,
                        "Load Rig File", "platform\\scripts\\sfm\\animset\\", "(*.py)")
            if  filename:
                
                toe=None
                collar=None
                with open(filename, 'r') as fin:
                    fin= fin.readlines()
                #######################################gets ver number    
                ver=fin[:5]#gets first 5 lines
                for i in ver:
                    if "Auto-Rigger v" in i:
                        b=i.find('v')
                        ver_num= float(i[b+1:b+4])
                        break

                ########################################


                if ver_num ==None:
                    self.error("This file is not compatable")
                    return 
                text=fin[-10:] #last ten lines
                
                if ver_num >=1.8:
                    
                    for i in text :
                        
                        if "boneList" in i and '[' in i:
                            
                            b=(i.find("["))
                            bonelist=ast.literal_eval(i[b:])###get the bone list        

                            index=self.handR.findText(bonelist[14])
                            self.handR.setCurrentIndex(index)
			    
                            index=self.handR.findText(bonelist[22])
                            self.bone_handL.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[1])
                            self.bone_spine0.setCurrentIndex(index)                           



                            index=self.handR.findText(bonelist[6])    
                            self.bone_head.setCurrentIndex(index)
			    
                            index=self.handR.findText(bonelist[5]) 
                            self.bone_neck.setCurrentIndex(index)
			    
                            index=self.handR.findText(bonelist[0])
                            self.bone_pelvis.setCurrentIndex(index)


                            index=self.handR.findText(bonelist[9])
                            self.bone_footR.setCurrentIndex(index)                            
                            index=self.handR.findText(bonelist[17])
                            self.bone_footL.setCurrentIndex(index)
                            

                        
                        if "BuildRig" in i:
			    b=i.find('(')
			    
			    e=i.find(')')
			    
                            inputlist=i[b+1:e].split(',')
			    
                            num=(int(inputlist[0])) #spine number
                            
                            axis=inputlist[4]
			    if '-'in axis:
				self.footroll_negative_checkbox.setChecked(True)			    
                            if  'z' in axis:
                                
                                self.footroll_checkbox.setChecked(True)
                                self.foot_z.setChecked(True)
                            elif 'x' in axis:
                                self.footroll_checkbox.setChecked(True)
                                self.foot_x.setChecked(True)
                            elif 'y' in axis:
                                self.footroll_checkbox.setChecked(True)
                                self.foot_y.setChecked(True)			
				
                            else:
                                self.footroll_checkbox.setChecked(False)

                            
                            if inputlist[1]=='True':#toe option
                                index=self.handR.findText(bonelist[18])
                                self.bone_toeL.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[10])
                                self.bone_toeR.setCurrentIndex(index)
                                self.toeoption.setChecked(True)
                                self.footroll_checkbox.setEnabled(True)
                            else:
                                self.toeoption.setChecked(False)
                                self.footroll_checkbox.setEnabled(False)
                                self.footroll_checkbox.setChecked(False)
                              ########################

                                
                            if inputlist[2]=='True':##collar option
                                index=self.handR.findText(bonelist[11])
                                self.bone_collarR.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[19])
                                self.bone_collarL.setCurrentIndex(index)
                                self.shoulderoption.setChecked(True)
                            else:
                                self.shoulderoption.setChecked(False)
                                
                            
			    if inputlist[5]=='True':#for rigfingers
				
				self.rig_fingers_checkbox.setChecked(True)
			    else:
				self.rig_fingers_checkbox.setChecked(False)
				
				
				
                              ##spine
                            
                            if num == 1:
                                self.sp1.setChecked(True)
                                index=self.handR.findText(bonelist[1])
                                self.bone_spine0.setCurrentIndex(index)
                            elif num == 2:
                                self.sp2.setChecked(True)
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)

                            elif num == 3:
                                self.sp3.setChecked(True)
                                index=self.handR.findText(bonelist[3])
                                self.bone_spine2.setCurrentIndex(index)
                                
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)
                            elif num == 4:
                                self.sp4.setChecked(True)
                                index=self.handR.findText(bonelist[4])
                                self.bone_spine3.setCurrentIndex(index)
                                
                                index=self.handR.findText(bonelist[3])
                                self.bone_spine2.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)
                                
                                index=self.handR.findText(bonelist[1])
                                self.bone_spine0.setCurrentIndex(index)
                                
                                
                            break



                if ver_num <1.5:
                    self.error("This version is no longer supported")
                    return
                if ver_num <1.8 and ver_num >= 1.5:
                    
                    for i in text :
                        
                        if "boneList" in i and '[' in i:
                            b=(i.find("["))
                            bonelist=ast.literal_eval(i[b:])###get the bone list        

                            index=self.handR.findText(bonelist[14])
                            self.handR.setCurrentIndex(index)
                            index=self.handR.findText(bonelist[22])
                            self.bone_handL.setCurrentIndex(index)


                                
                            index=self.handR.findText(bonelist[7])
                            self.bone_upperlegR.setCurrentIndex(index)



                            index=self.handR.findText(bonelist[15])
                            self.bone_upperlegL.setCurrentIndex(index)
                            index=self.handR.findText(bonelist[8])
                            self.bone_lowerlegR.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[16])
                            self.bone_lowerlegL.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[20])
                            self.bone_upperarmL.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[12])
                            self.upperarmR.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[21])
                            self.bone_lowerarmL.setCurrentIndex(index)
                            index=self.handR.findText(bonelist[13])
                            self.bone_lowerarmR.setCurrentIndex(index)

                            index=self.handR.findText(bonelist[1])
                            self.bone_spine0.setCurrentIndex(index)
                            



                            index=self.handR.findText(bonelist[6])    
                            self.bone_head.setCurrentIndex(index)
                            index=self.handR.findText(bonelist[5]) 
                            self.bone_neck.setCurrentIndex(index)
                            index=self.handR.findText(bonelist[0])
                            self.bone_pelvis.setCurrentIndex(index)


                            index=self.handR.findText(bonelist[9])
                            self.bone_footR.setCurrentIndex(index)                            
                            index=self.handR.findText(bonelist[17])
                            self.bone_footL.setCurrentIndex(index)                    

                        
                        if "BuildRig" in i:
                            
                            num=(int(i[9])) #spine number
                           
                            return
                            if i[11]=='T':#toe option
                                index=self.handR.findText(bonelist[18])
                                self.bone_toeL.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[10])
                                self.bone_toeR.setCurrentIndex(index)
                            else:
                                self.toeoption.setChecked(False)
                              ########################

                                
                            if i[16]=="T":##collar option
                                index=self.handR.findText(bonelist[11])
                                self.bone_collarR.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[19])
                                self.bone_collarL.setCurrentIndex(index)
                            else:
                                self.shoulderoption.setChecked(False)

                              ##spine  
                            if num == 2:
                                self.sp2.setChecked(True)
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)

                            elif num == 3:
                                self.sp3.setChecked(True)
                                index=self.handR.findText(bonelist[3])
                                self.bone_spine2.setCurrentIndex(index)
                                
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)
                            elif num == 4:
                                self.sp4.setChecked(True)
                                index=self.handR.findText(bonelist[4])
                                self.bone_spine3.setCurrentIndex(index)
                                
                                index=self.handR.findText(bonelist[3])
                                self.bone_spine2.setCurrentIndex(index)
                                index=self.handR.findText(bonelist[2])
                                self.bone_spine1.setCurrentIndex(index)
                            break

                                






   

                     
        except any as e:
            print e
            return

                                                      
                            
        self.hide()
     



##============================================
##auto finds  and selects the right bone name 
##============================================
    def find(self,lst):
        #common bone names can add more if need to
        handr_list = ['hand_r', 'r_hand', 'r hand','hand r','handr','wrist_r', 'r_wrist', 'r wrist','wrist r','wristr']
        handL_list = ['hand_l', 'l_hand', 'l hand','hand l','wrist_l', 'l_wrist', 'l wrist','wrist l','wristl','handl']
        
        collarR_list=['collarr','r_clavicle','clavicle_r','clavicle r','r clavicle','r_collar','collar_r','collar r','r collar','r_shoulder','shoulder_r','shoulder r','r shoulder']
        collarL_list=['collarl','l_clavicle','clavicle_l','clavicle l','l clavicle','l_collar','collar_l','collar l','l collar','l_shoulder','shoulder_l','shoulder l','l shoulder']
        


        for name in handr_list:
            for i in lst:
                if name in i.lower():
                    index=self.bone_head.findText(i)
                    self.handR.setCurrentIndex(index)

                    
        for name in handL_list:
            for i in lst:
                if name in i.lower():
                    index=self.bone_head.findText(i)
                    self.bone_handL.setCurrentIndex(index)
                    break

                    
                    
        for name in collarR_list:
            for i in lst:
                if name in i.lower():
                    index=self.bone_head.findText(i)
                    self.bone_collarR.setCurrentIndex(index)
                    break

        for name in collarL_list:
            for i in lst:
                if name in i.lower():
                    index=self.bone_head.findText(i)
                    self.bone_collarL.setCurrentIndex(index)
                    break

    

        
############ a differnet way to find common bone name



        for name in lst:

            if name.lower().find('spine0')!=-1 or name.lower().find('spine_0')!=-1 or name.lower().find('spine')!=-1  :
                index = self.bone_head.findText(name)
                self.bone_spine0.setCurrentIndex(index)
                break



        for name in lst:
            
            if name.lower().find('bip_head')!=-1 or name.lower().find('head')!=-1:
                index=self.bone_head.findText(name)
                self.bone_head.setCurrentIndex(index)
                break



                    
        for name in lst:
            

                
                
            if name.lower().find('neck')!=-1:
                index=self.bone_head.findText(name)
                self.bone_neck.setCurrentIndex(index)
                
            if name.lower().find('pelvis')!=-1:
                index=self.bone_head.findText(name)
                self.bone_pelvis.setCurrentIndex(index)
                

            
            if name.lower().find('spine1')!=-1 or name.lower().find('spine_1')!=-1:
                index=self.bone_head.findText(name)
                self.bone_spine1.setCurrentIndex(index)
                
            if name.lower().find('spine2')!=-1 or name.lower().find('spine_2')!=-1:
                index=self.bone_head.findText(name)
                self.bone_spine2.setCurrentIndex(index)
                
            if name.lower().find('spine3')!=-1 or name.lower().find('spine4')!=-1 or name.lower().find('spine_3')!=-1:
                index=self.bone_head.findText(name)
                self.bone_spine3.setCurrentIndex(index)


            if  name.lower().find('footL')!=-1 or name.lower().find('l_foot')!=-1 or name.lower().find('foot_l')!=-1 or name.lower().find('foot l')!=-1 or name.lower().find('l foot')!=-1 or name.lower().find('ankle_l')!=-1 or name.lower().find('ankle l')!=-1 or name.lower().find('l ankle')!=-1:
                index=self.bone_head.findText(name)
                self.bone_footL.setCurrentIndex(index)
                
            if  name.lower().find('footr')!=-1 or name.lower().find('r_foot')!=-1 or name.lower().find('foot_r')!=-1 or name.lower().find('foot r')!=-1 or name.lower().find('r foot')!=-1 or name.lower().find('ankle_r')!=-1 or name.lower().find('ankle r')!=-1 or name.lower().find('r ankle')!=-1:
                index=self.bone_head.findText(name)
                self.bone_footR.setCurrentIndex(index)



            if  name.lower().find('toer')!=-1 or name.lower().find('r_toe')!=-1 or name.lower().find('toe_r')!=-1 or name.lower().find('toe r')!=-1 or name.lower().find('r toe')!=-1 or name.lower().find('toebase_r')!=-1:
                index=self.bone_head.findText(name)
                self.bone_toeR.setCurrentIndex(index)


            if  name.lower().find('toel')!=-1 or name.lower().find('l_toe')!=-1 or name.lower().find('toe_l')!=-1 or name.lower().find('toe l')!=-1 or name.lower().find('l toe')!=-1 or name.lower().find('toebase_l')!=-1:
                index=self.bone_head.findText(name)
                self.bone_toeL.setCurrentIndex(index)









	    # auto picks the parent and grandparent for ik 
    def autofind(self,child,parent,grandparent):
        #print num
	#print child.currentText()
	boneRoot = self.bonename_to_obj[child.currentText()]
	
	#print str(boneRoot.GetParent().GetParent())
	#help(boneRoot)
	if "bone" not in str(boneRoot.GetParent().GetParent()):
		
		return	
	
	
	b=str(boneRoot.GetParent().GetName()).find('(')
	e=str(boneRoot.GetParent().GetName()).find(')')
	boneparent=str(boneRoot.GetParent().GetName())[b+1:e]	
	
	
	b=str(boneRoot.GetParent().GetParent().GetName()).find('(')
	e=str(boneRoot.GetParent().GetParent().GetName()).find(')')
	bonegrandparent=str(boneRoot.GetParent().GetParent().GetName())[b+1:e]	
	
	
	parent.setCurrentIndex(parent.findText(boneparent))
	
	grandparent.setCurrentIndex(parent.findText(bonegrandparent))
	
    def Message(self,text):
        #message box

        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information,
                "Success", text,
                QtGui.QMessageBox.NoButton, self)
        font = QtGui.QFont()
        font.setPointSize(11)
        msgBox.setFont(font)
        msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
        if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:pass



    def error(self,e):
        #error box

        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                "ERROR", "File could not be created error: \n\n"+str(e),
                QtGui.QMessageBox.NoButton, self)

        font = QtGui.QFont()
        font.setPointSize(11)
        msgBox.setFont(font)
        msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
        if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:pass





    def main(self):

        #gets bone name from user
        head=       self.bone_head.currentText()
        footL=      self.bone_footL.currentText()
        footR=      self.bone_footR.currentText()
        spine0=     self.bone_spine0.currentText()
        spine1=     self.bone_spine1.currentText()
        spine2=     self.bone_spine2.currentText()
        spine3=     self.bone_spine3.currentText()
        neck=       self.bone_neck.currentText()
        lowarmL=    self.bone_lowerarmL.currentText()
        lowarmR=    self.bone_lowerarmR.currentText()
        uparmL=     self.bone_upperarmL.currentText()
        uparmR=     self.upperarmR.currentText()
        pelvis=     self.bone_pelvis.currentText()
        uplegR=     self.bone_upperlegR.currentText()
        uplegL=     self.bone_upperlegL.currentText()
        lowlegR=    self.bone_lowerlegR.currentText()
        lowlegL=    self.bone_lowerlegL.currentText()
        footR=      self.bone_footR.currentText()
        footL=      self.bone_footL.currentText()
        toeR=       self.bone_toeR.currentText()
        toeL=       self.bone_toeL.currentText()
        handR=      self.handR.currentText()
        handL=      self.bone_handL.currentText()
        collR=      self.bone_collarR.currentText()
        collL=      self.bone_collarL.currentText()
#===============================================================================================================================
#the script file template
#===============================================================================================================================



        script="""
#created with Auto-Rigger v1.9 for biped models
#BY http://steamcommunity.com/id/OMGTheresABearInMyOatmeal/
#This is just a modified version of valves' biped simple script.

import vs
import random
from collections import OrderedDict

#==================================================================================================
def AddValidObjectToList( objectList, obj ):
    if ( obj != None ): objectList.append( obj )


#==================================================================================================
def HideControlGroups( rig, rootGroup, *groupNames ):
    for name in groupNames:
        group = rootGroup.FindChildByName( name, False )
        if ( group != None ):
            rig.HideControlGroup( group )


def CreateOrientConstraint( target, slave, bCreateControls=True, group=None ) :
    ''' Method for creating a single target orient constraint '''
    
    if ( target == None ):
        return

    targetDag = sfmUtils.GetDagFromNameOrObject( target )
    slaveDag = sfmUtils.GetDagFromNameOrObject( slave )
    
    sfm.PushSelection()
    sfmUtils.SelectDagList( [ targetDag, slaveDag ] )
    
    
    orientConstraintTarget = sfm.OrientConstraint( controls=bCreateControls )
    
    if ( group != None ):

        if ( orientConstraintTarget != None ):
            orientWeightControl = orientConstraintTarget.FindWeightControl()
            if ( orientWeightControl != None ):
                group.AddControl( orientWeightControl )
            
    sfm.PopSelection()
    return

#==================================================================================================
# this is a recursive function for riging all child dags of a parent dag
#==================================================================================================
rig_fingers=OrderedDict()
dag_fingers=[]
def rigfingers(dag,rig_root):

    if dag.GetChildCount()>0:
        for index in range(dag.GetChildCount()):
           
           # print "parent " +str(dag.GetChild(index).GetName())+ " to "+ parentname
            
            dag_fingers.append(dag.GetChild(index))
            temp=dag_fingers[-1].GetName()
            FingerName=temp[temp.find("(")+1:temp.find(")")]
            fig=sfmUtils.CreateConstrainedHandle( "RIG_"+FingerName,  dag_fingers[-1]   ,    bCreateControls=False )
            
            rig_fingers[fig]=rig_root
                  
           # CreateOrientConstraint( fig,dag_fingers[-1])
            
            rigfingers(dag_fingers[-1],fig)
    return 


def parent_rig_fingers(rig_root,fingerdict):


    for child in fingerdict:
        sfmUtils.ParentMaintainWorld( child,fingerdict[child] )
            



    






#==================================================================================================
# Create the reverse foot control and operators for the foot on the specified side
#==================================================================================================
def CreateReverseFoot( controlName, sideName, gameModel, animSet, shot, helperControlGroup, footControlGroup,footroll ) :

    # Cannot create foot controls without heel position, so check for that first
    #heelAttachName = "pvt_heel_" + sideName
    if (  footroll == None ):
        #print "Could not create foot control " + controlName + ", model is missing heel attachment point: " + heelAttachName;
        return None

    footRollDefault = 0.5
    if (footroll=="x"):
        rotationAxis = vs.Vector( 1, 0, 0 )
    elif (footroll=="y"):
        rotationAxis = vs.Vector( 0, 1, 0 )
    elif (footroll=="z"):
        rotationAxis = vs.Vector( 0, 0, 1 )
    elif (footroll=="-x"):
        rotationAxis = vs.Vector( -1, 0, 0 )
    elif (footroll=="-y"):
        rotationAxis = vs.Vector( 0, -1, 0 )
    elif (footroll=="-z"):
        rotationAxis = vs.Vector( 0, 0, -1 )	
    else: return None
    # Construct the name of the dag nodes of the foot and toe for the specified side
    footName = "rig_foot_" + sideName
    toeName = "rig_toe_" + sideName

    # Get the world space position and orientation of the foot and toe
    footPos = sfm.GetPosition( footName )
    footRot = sfm.GetRotation( footName )
    toePos = sfm.GetPosition( toeName )

    # Setup the reverse foot hierarchy such that the foot is the parent of all the foot transforms, the
    # reverse heel is the parent of the heel, so it can be used for rotations around the ball of the
    # foot that will move the heel, the heel is the parent of the foot IK handle so that it can perform
    # rotations around the heel and move the foot IK handle, resulting in moving all the foot bones.
    # root
    #   + rig_foot_R
    #       + rig_knee_R
    #       + rig_reverseHeel_R
    #           + rig_heel_R
    #               + rig_footIK_R


    # Construct the reverse heel joint this will be used to rotate the heel around the toe, and as
    # such is positioned at the toe, but using the rotation of the foot which will be its parent,
    # so that it has no local rotation once parented to the foot.
    reverseHeelName = "rig_reverseHeel_" + sideName
    reverseHeelDag = sfm.CreateRigHandle( reverseHeelName, pos=toePos, rot=footRot, rotControl=False )
    sfmUtils.Parent( reverseHeelName, footName, vs.REPARENT_LOGS_OVERWRITE )



    # Construct the heel joint, this will be used to rotate the foot around the back of the heel so it
    # is created at the heel location (offset from the foot) and also given the rotation of its parent.
    heelName = "rig_heel_" + sideName
    #vecHeelPos = gameModel.ComputeAttachmentPosition( heelAttachName )
   # heelPos = [ vecHeelPos.x, vecHeelPos.y, vecHeelPos.z ]
    heelRot = sfm.GetRotation( reverseHeelName )
    heelDag = sfm.CreateRigHandle( heelName, pos=footPos, rot=heelRot, posControl=True, rotControl=False )
    sfmUtils.Parent( heelName, reverseHeelName, vs.REPARENT_LOGS_OVERWRITE )

    # Create the ik handle which will be used as the target for the ik chain for the leg
    ikHandleName = "rig_footIK_" + sideName
    ikHandleDag = sfmUtils.CreateHandleAt( ikHandleName, footName )
    sfmUtils.Parent( ikHandleName, heelName, vs.REPARENT_LOGS_OVERWRITE )

    # Create an orient constraint which causes the toe's orientation to match the foot's orientation
    footRollControlName = controlName + "_" + sideName
    toeOrientTarget = sfm.OrientConstraint( footName, toeName, mo=True, controls=False )
    footRollControl, footRollValue = sfmUtils.CreateControlledValue( footRollControlName, "value", vs.AT_FLOAT, footRollDefault, animSet, shot )

    # Create the expressions to re-map the footroll slider value for use in the constraint and rotation operators
    toeOrientExprName = "expr_toeOrientEnable_" + sideName
    toeOrientExpr = sfmUtils.CreateExpression( toeOrientExprName, "inrange( footRoll, 0.5001, 1.0 )", animSet )
    toeOrientExpr.SetValue( "footRoll", footRollDefault )

    toeRotateExprName = "expr_toeRotation_" + sideName
    toeRotateExpr = sfmUtils.CreateExpression( toeRotateExprName, "max( 0, (footRoll - 0.5) ) * 140", animSet )
    toeRotateExpr.SetValue( "footRoll", footRollDefault )

    heelRotateExprName = "expr_heelRotation_" + sideName
    heelRotateExpr = sfmUtils.CreateExpression( heelRotateExprName, "max( 0, (0.5 - footRoll) ) * -100", animSet )
    heelRotateExpr.SetValue( "footRoll", footRollDefault )

    # Create a connection from the footroll value to all of the expressions that require it
    footRollConnName = "conn_footRoll_" + sideName
    footRollConn = sfmUtils.CreateConnection( footRollConnName, footRollValue, "value", animSet )
    footRollConn.AddOutput( toeOrientExpr, "footRoll" )
    footRollConn.AddOutput( toeRotateExpr, "footRoll" )
    footRollConn.AddOutput( heelRotateExpr, "footRoll" )

    # Create the connection from the toe orientation enable expression to the target weight of the
    # toe orientation constraint, this will turn the constraint on an off based on the footRoll value
    toeOrientConnName = "conn_toeOrientExpr_" + sideName;
    toeOrientConn = sfmUtils.CreateConnection( toeOrientConnName, toeOrientExpr, "result", animSet )
    toeOrientConn.AddOutput( toeOrientTarget, "targetWeight" )

    # Create a rotation constraint to drive the toe rotation and connect its input to the
    # toe rotation expression and connect its output to the reverse heel dag's orientation
    toeRotateConstraintName = "rotationConstraint_toe_" + sideName
    toeRotateConstraint = sfmUtils.CreateRotationConstraint( toeRotateConstraintName, rotationAxis, reverseHeelDag, animSet )

    toeRotateExprConnName = "conn_toeRotateExpr_" + sideName
    toeRotateExprConn = sfmUtils.CreateConnection( toeRotateExprConnName, toeRotateExpr, "result", animSet )
    toeRotateExprConn.AddOutput( toeRotateConstraint, "rotations", 0 );

    # Create a rotation constraint to drive the heel rotation and connect its input to the
    # heel rotation expression and connect its output to the heel dag's orientation
    heelRotateConstraintName = "rotationConstraint_heel_" + sideName
    heelRotateConstraint = sfmUtils.CreateRotationConstraint( heelRotateConstraintName, rotationAxis, heelDag, animSet )

    heelRotateExprConnName = "conn_heelRotateExpr_" + sideName
    heelRotateExprConn = sfmUtils.CreateConnection( heelRotateExprConnName, heelRotateExpr, "result", animSet )
    heelRotateExprConn.AddOutput( heelRotateConstraint, "rotations", 0 )

    if ( helperControlGroup != None ):
        sfmUtils.AddDagControlsToGroup( helperControlGroup, reverseHeelDag, ikHandleDag, heelDag )

    if ( footControlGroup != None ):
        footControlGroup.AddControl( footRollControl )

    return ikHandleDag


#==================================================================================================
# Compute the direction from boneA to boneB
#==================================================================================================
def ComputeVectorBetweenBones( boneA, boneB, scaleFactor ):

    vPosA = vs.Vector( 0, 0, 0 )
    boneA.GetAbsPosition( vPosA )

    vPosB = vs.Vector( 0, 0, 0 )
    boneB.GetAbsPosition( vPosB )

    vDir = vs.Vector( 0, 0, 0 )
    vs.mathlib.VectorSubtract( vPosB, vPosA, vDir )
    vDir.NormalizeInPlace()

    vScaledDir = vs.Vector( 0, 0, 0 )
    vs.mathlib.VectorScale( vDir, scaleFactor, vScaledDir )

    return vScaledDir


#==================================================================================================
# Build a simple ik rig for the currently selected animation set
#==================================================================================================
def BuildRig(num,toe,collar,bone,footroll,fingeropton,handpreset):

    # Get the currently selected animation set and shot
    shot = sfm.GetCurrentShot()
    animSet = sfm.GetCurrentAnimationSet()
    gameModel = animSet.gameModel
    rootGroup = animSet.GetRootControlGroup()

    # Start the biped rig to which all of the controls and constraints will be added
    rig = sfm.BeginRig( "rig_biped_" + animSet.GetName() + str(random.randint(1,100)) );
    if ( rig == None ):
        return

    # Change the operation mode to passthrough so changes chan be made temporarily
    sfm.SetOperationMode( "Pass" )

    # Move everything into the reference pose
    sfm.SelectAll()
    sfm.SetReferencePose()

    #==============================================================================================
    # Find the dag nodes for all of the bones in the model which will be used by the script
    #==============================================================================================
    boneRoot      = sfmUtils.FindFirstDag( [ "RootTransform" ], True )
    bonePelvis    = sfmUtils.FindFirstDag( [ bone[0]  ], True )

    


    if num==4:
        
        boneSpine0    = sfmUtils.FindFirstDag( [  bone[1]  ], True )
        boneSpine1    = sfmUtils.FindFirstDag( [  bone[2]   ], True )
        boneSpine2    = sfmUtils.FindFirstDag( [  bone[3] ], True )
        boneSpine3    = sfmUtils.FindFirstDag( [  bone[4]   ], True )

        rigSpine0  = sfmUtils.CreateConstrainedHandle( "rig_spine_0",  boneSpine0,  bCreateControls=False )
        rigSpine1  = sfmUtils.CreateConstrainedHandle( "rig_spine_1",  boneSpine1,  bCreateControls=False )
        rigSpine2  = sfmUtils.CreateConstrainedHandle( "rig_spine_2",  boneSpine2,  bCreateControls=False )
        rigChest   = sfmUtils.CreateConstrainedHandle( "rig_chest",    boneSpine3,  bCreateControls=False )



        
    elif num==3:
        boneSpine0    = sfmUtils.FindFirstDag( [ bone[1]  ], True )
        boneSpine1    = sfmUtils.FindFirstDag( [ bone[2] ], True )
        boneSpine2    = sfmUtils.FindFirstDag( [ bone[3]], True )

        rigSpine0  = sfmUtils.CreateConstrainedHandle( "rig_spine_0",  boneSpine0,  bCreateControls=False )
        rigSpine1  = sfmUtils.CreateConstrainedHandle( "rig_spine_1",  boneSpine1,  bCreateControls=False )
        rigSpine2  = sfmUtils.CreateConstrainedHandle( "rig_spine_2",  boneSpine2,  bCreateControls=False )
        rigChest   = "null"


        


        
    elif num==2:
        boneSpine0    = sfmUtils.FindFirstDag( [ bone[1]  ], True )
        rigSpine0  = sfmUtils.CreateConstrainedHandle( "rig_spine_0",  boneSpine0,  bCreateControls=False )
        boneSpine1    = sfmUtils.FindFirstDag( [ bone[2]  ], True )
        rigSpine1  = sfmUtils.CreateConstrainedHandle( "rig_spine_1",  boneSpine1,  bCreateControls=False )
        rigSpine2  = "null"
        rigChest   = "null"
        
    elif num==1:
        boneSpine0    = sfmUtils.FindFirstDag( [ bone[1]  ], True )
        rigSpine0  = sfmUtils.CreateConstrainedHandle( "rig_spine_0",  boneSpine0,  bCreateControls=False )

        rigSpine1  = "null"
        rigSpine2  = "null"
        rigChest   = "null"
        
    boneNeck      = sfmUtils.FindFirstDag( [ bone[5] ], True )
    boneHead      = sfmUtils.FindFirstDag( [ bone[6]  ], True )
    boneUpperLegR = sfmUtils.FindFirstDag( [ bone[7]  ], True )
    boneLowerLegR = sfmUtils.FindFirstDag( [ bone[8] ], True )
    boneFootR     = sfmUtils.FindFirstDag( [ bone[9]  ], True )


    if toe:
        boneToeR      = sfmUtils.FindFirstDag( [ bone[10] ], True )
        boneToeL      = sfmUtils.FindFirstDag( [ bone[18] ], True )
        rigToeR    = sfmUtils.CreateConstrainedHandle( "rig_toe_R",    boneToeR,    bCreateControls=False )
        rigToeL    = sfmUtils.CreateConstrainedHandle( "rig_toe_L",    boneToeL,    bCreateControls=False )
    else:
        rigToeR = "null"
        rigToeL = "null"





    if collar:
        boneCollarR   = sfmUtils.FindFirstDag( [ bone[11] ], True )
        boneCollarL   = sfmUtils.FindFirstDag( [ bone[19] ], True )
        rigCollarR = sfmUtils.CreateConstrainedHandle( "rig_collar_R", boneCollarR, bCreateControls=False )
        rigCollarL = sfmUtils.CreateConstrainedHandle( "rig_collar_L", boneCollarL, bCreateControls=False )
    else:
        rigCollarR = "null"
        rigCollarL = "null"




    boneUpperArmR = sfmUtils.FindFirstDag( [ bone[12]  ], True )
    boneLowerArmR = sfmUtils.FindFirstDag( [ bone[13]  ], True )
    boneHandR     = sfmUtils.FindFirstDag( [ bone[14]  ], True )
    boneUpperLegL = sfmUtils.FindFirstDag( [ bone[15]  ], True )
    boneLowerLegL = sfmUtils.FindFirstDag( [ bone[16]  ], True )
    boneFootL     = sfmUtils.FindFirstDag( [ bone[17]  ], True )    
    boneUpperArmL = sfmUtils.FindFirstDag( [ bone[20]  ], True )
    boneLowerArmL = sfmUtils.FindFirstDag( [ bone[21]  ], True )
    boneHandL     = sfmUtils.FindFirstDag( [ bone[22]  ], True )

















    

    #==============================================================================================
    # Create the rig handles and constrain them to existing bones
    #==============================================================================================
    rigRoot    = sfmUtils.CreateConstrainedHandle( "rig_root",     boneRoot,    bCreateControls=False )
    rigPelvis  = sfmUtils.CreateConstrainedHandle( "rig_pelvis",   bonePelvis,  bCreateControls=False )
    rigNeck    = sfmUtils.CreateConstrainedHandle( "rig_neck",     boneNeck,    bCreateControls=False )
    rigHead    = sfmUtils.CreateConstrainedHandle( "rig_head",     boneHead,    bCreateControls=False )
    rigFootR   = sfmUtils.CreateConstrainedHandle( "rig_foot_R",   boneFootR,   bCreateControls=False )
    rigHandR   = sfmUtils.CreateConstrainedHandle( "rig_hand_R",   boneHandR,   bCreateControls=False )
    rigFootL   = sfmUtils.CreateConstrainedHandle( "rig_foot_L",   boneFootL,   bCreateControls=False )
    rigHandL   = sfmUtils.CreateConstrainedHandle( "rig_hand_L",   boneHandL,   bCreateControls=False )


    # Use the direction from the heel to the toe to compute the knee offsets,
    # this makes the knee offset indpendent of the inital orientation of the model.
    if toe:
        vKneeOffsetR = ComputeVectorBetweenBones( boneFootR, boneToeR, 10 )
        vKneeOffsetL = ComputeVectorBetweenBones( boneFootL, boneToeL, 10 )
    else:
        vKneeOffsetR = ComputeVectorBetweenBones( boneFootR, boneFootR, 10 )
        vKneeOffsetL = ComputeVectorBetweenBones( boneFootL, boneFootL, 10 )


    rigKneeR   = sfmUtils.CreateOffsetHandle( "rig_knee_R",  boneLowerLegR, vKneeOffsetR,  bCreateControls=False )
    rigKneeL   = sfmUtils.CreateOffsetHandle( "rig_knee_L",  boneLowerLegL, vKneeOffsetL,  bCreateControls=False )
    rigElbowR  = sfmUtils.CreateOffsetHandle( "rig_elbow_R", boneLowerArmR, -vKneeOffsetR,  bCreateControls=False )
    rigElbowL  = sfmUtils.CreateOffsetHandle( "rig_elbow_L", boneLowerArmL, -vKneeOffsetL,  bCreateControls=False )

    # Create a helper handle which will remain constrained to the each foot position that can be used for parenting.
    rigFootHelperR = sfmUtils.CreateConstrainedHandle( "rig_footHelper_R", boneFootR, bCreateControls=False )
    rigFootHelperL = sfmUtils.CreateConstrainedHandle( "rig_footHelper_L", boneFootL, bCreateControls=False )

    # Create a list of all of the rig dags
    allRigHandles=[]
    allRigHandles1 = [ rigRoot, rigPelvis, rigSpine0, rigSpine1, rigSpine2, rigChest, rigNeck, rigHead,
                      rigCollarR, rigElbowR, rigHandR, rigKneeR, rigFootR, rigToeR,
                      rigCollarL, rigElbowL, rigHandL, rigKneeL,rigFootL, rigToeL ];
    for i in allRigHandles1:
        if i !="null":
            allRigHandles.append(i)



    #for fingers

    
    if (fingeropton):
        global rig_fingers,dag_fingers
        
        rigfingers(boneHandR,rigHandR)
        rig_finger_right=rig_fingers.copy()
        bone_finger_right=dag_fingers[:]
        
        rig_fingers.clear()
        del dag_fingers[:]       
        
        rigfingers(boneHandL,rigHandL)
        rig_finger_left=rig_fingers.copy()
        bone_finger_left=dag_fingers[:]

        
    allRigHandles.extend(rig_finger_left.keys()+rig_finger_right.keys())
    #==============================================================================================
    # Generate the world space logs for the rig handles and remove the constraints
    #==============================================================================================
    sfm.ClearSelection()
    sfmUtils.SelectDagList( allRigHandles )
    sfm.GenerateSamples()
    sfm.RemoveConstraints()
    


        

    #==============================================================================================
    # Build the rig handle hierarchy
    #==============================================================================================
    sfmUtils.ParentMaintainWorld( rigPelvis,        rigRoot )
    sfmUtils.ParentMaintainWorld( rigSpine0,        rigPelvis )


    if num==4:
        sfmUtils.ParentMaintainWorld( rigSpine1,        rigSpine0 )
        sfmUtils.ParentMaintainWorld( rigSpine2,        rigSpine1 )
        sfmUtils.ParentMaintainWorld( rigChest,         rigSpine2 )
        sfmUtils.ParentMaintainWorld( rigNeck,          rigChest )
        if collar:
            sfmUtils.ParentMaintainWorld( rigCollarR,       rigChest )
            sfmUtils.ParentMaintainWorld( rigCollarL,       rigChest )
        else:
            sfmUtils.ParentMaintainWorld( rigElbowR,       rigChest )
            sfmUtils.ParentMaintainWorld( rigElbowL,       rigChest )
            
    elif num==3:
        sfmUtils.ParentMaintainWorld( rigSpine1,        rigSpine0 )
        sfmUtils.ParentMaintainWorld( rigSpine2,        rigSpine1 )
        sfmUtils.ParentMaintainWorld( rigNeck,         rigSpine2 )

        if collar:
            sfmUtils.ParentMaintainWorld( rigCollarR,       rigSpine2 )
            sfmUtils.ParentMaintainWorld( rigCollarL,       rigSpine2 )
        else:
            sfmUtils.ParentMaintainWorld( rigElbowR,       rigSpine2 )
            sfmUtils.ParentMaintainWorld( rigElbowL,       rigSpine2 )


    elif num==2:
        sfmUtils.ParentMaintainWorld( rigSpine1,        rigSpine0 )
        sfmUtils.ParentMaintainWorld( rigNeck,        rigSpine1 )
          

        if collar:
            sfmUtils.ParentMaintainWorld( rigCollarR,       rigSpine1 )
            sfmUtils.ParentMaintainWorld( rigCollarL,       rigSpine1 )
        else:
            sfmUtils.ParentMaintainWorld( rigElbowR,       rigSpine1 )
            sfmUtils.ParentMaintainWorld( rigElbowL,       rigSpine1 )

            

    elif num==1:
        
        sfmUtils.ParentMaintainWorld( rigNeck,        rigSpine0 )
          

        if collar:
            sfmUtils.ParentMaintainWorld( rigCollarR,       rigSpine0 )
            sfmUtils.ParentMaintainWorld( rigCollarL,       rigSpine0 )
        else:
            sfmUtils.ParentMaintainWorld( rigElbowR,       rigSpine0 )
            sfmUtils.ParentMaintainWorld( rigElbowL,       rigSpine0 )

        
      
    sfmUtils.ParentMaintainWorld( rigHead,          rigNeck )
    sfmUtils.ParentMaintainWorld( rigFootHelperR,   rigRoot )
    sfmUtils.ParentMaintainWorld( rigFootHelperL,   rigRoot )
    sfmUtils.ParentMaintainWorld( rigFootR,         rigRoot )
    sfmUtils.ParentMaintainWorld( rigFootL,         rigRoot )



    
    sfmUtils.ParentMaintainWorld( rigKneeR,         rigFootR )
    sfmUtils.ParentMaintainWorld( rigKneeL,         rigFootL )
    if toe:
        sfmUtils.ParentMaintainWorld( rigToeR,          rigFootR )
        sfmUtils.ParentMaintainWorld( rigToeL,          rigFootL )

    if collar:
        sfmUtils.ParentMaintainWorld( rigElbowR,        rigCollarR )
        sfmUtils.ParentMaintainWorld( rigElbowL,        rigCollarL )
        
    sfmUtils.ParentMaintainWorld( rigHandR,	    rigRoot )


    sfmUtils.ParentMaintainWorld( rigHandL,	    rigRoot )





######for fingers
    if (fingeropton):
        parent_rig_fingers(rigHandR,rig_finger_right)
        parent_rig_fingers(rigHandL,rig_finger_left)











    






    

    # Create the hips control, this allows a pelvis rotation that does not effect the spine,
    # it is only used for rotation so a position control is not created. Additionally add the
    # new control to the selection so the that set default call operates on it too.
    rigHips = sfmUtils.CreateHandleAt( "rig_hips", rigPelvis, False, True )
    sfmUtils.Parent( rigHips, rigPelvis, vs.REPARENT_LOGS_OVERWRITE )
    sfm.SelectDag( rigHips )

    # Set the defaults of the rig transforms to the current locations. Defaults are stored in local
    # space, so while the parent operation tries to preserve default values it is cleaner to just
    # set them once the final hierarchy is constructed.
    sfm.SetDefault()


    #==============================================================================================
    # Create the reverse foot controls for both the left and right foot
    #==============================================================================================
    rigLegsGroup = rootGroup.CreateControlGroup( "RigLegs" )
    rigHelpersGroup = rootGroup.CreateControlGroup( "RigHelpers" )
    rigHelpersGroup.SetVisible( False )
    rigHelpersGroup.SetSnappable( False )

    footIKTargetR = rigFootR
    footIkTargetL = rigFootL

    if ( gameModel != None ) :
        footRollIkTargetR = CreateReverseFoot( "rig_footRoll", "R", gameModel, animSet, shot, rigHelpersGroup, rigLegsGroup,footroll)
        footRollIkTargetL = CreateReverseFoot( "rig_footRoll", "L", gameModel, animSet, shot, rigHelpersGroup, rigLegsGroup,footroll )
        if ( footRollIkTargetR != None ) :
            footIKTargetR = footRollIkTargetR
        if ( footRollIkTargetL != None ) :
            footIkTargetL = footRollIkTargetL


    #==============================================================================================
    # Create constraints to drive the bone transforms using the rig handles
    #==============================================================================================



            
    # The following bones are simply constrained directly to a rig handle
    sfmUtils.CreatePointOrientConstraint( rigRoot,      boneRoot        )
    sfmUtils.CreatePointOrientConstraint( rigHips,      bonePelvis      )
    sfmUtils.CreatePointOrientConstraint( rigSpine0,    boneSpine0      )
    
    if num==4:
        sfmUtils.CreatePointOrientConstraint( rigSpine2,    boneSpine2      )
        sfmUtils.CreatePointOrientConstraint( rigChest,     boneSpine3      )
    elif num==3:
        sfmUtils.CreatePointOrientConstraint( rigSpine2,    boneSpine2      )
    elif num ==2:
        sfmUtils.CreatePointOrientConstraint( rigSpine1,    boneSpine1      )
        


        
    sfmUtils.CreatePointOrientConstraint( rigNeck,      boneNeck        )
    sfmUtils.CreatePointOrientConstraint( rigHead,      boneHead        )
    if collar:
        sfmUtils.CreatePointOrientConstraint( rigCollarR,   boneCollarR     )
        sfmUtils.CreatePointOrientConstraint( rigCollarL,   boneCollarL     )

    if toe:
        CreateOrientConstraint( rigToeR,      boneToeR        )
        CreateOrientConstraint( rigToeL,      boneToeL        )


##fingers
    if (fingeropton):
        index=0
        for Rig in rig_finger_right:
            CreateOrientConstraint( Rig,bone_finger_right[index])
            index+=1

        index=0
        for Rig in rig_finger_left:
            CreateOrientConstraint( Rig,bone_finger_left[index])
            index+=1









        

    # Create ik constraints for the arms and legs that will control the rotation of the hip / knee and
    # upper arm / elbow joints based on the position of the foot and hand respectively.



    
    sfmUtils.BuildArmLeg( rigKneeR,  footIKTargetR, boneUpperLegR,  boneFootR, True )
    sfmUtils.BuildArmLeg( rigKneeL,  footIkTargetL, boneUpperLegL,  boneFootL, True )
    sfmUtils.BuildArmLeg( rigElbowR, rigHandR,      boneUpperArmR,  boneHandR, True )
    sfmUtils.BuildArmLeg( rigElbowL, rigHandL,      boneUpperArmL,  boneHandL, True )


    #==============================================================================================
    # Create handles for the important attachment points
    #==============================================================================================
    attachmentGroup = rootGroup.CreateControlGroup( "Attachments" )
    attachmentGroup.SetVisible( False )

    sfmUtils.CreateAttachmentHandleInGroup( "pvt_heel_R",       attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_toe_R",        attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_outerFoot_R",  attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_innerFoot_R",  attachmentGroup )

    sfmUtils.CreateAttachmentHandleInGroup( "pvt_heel_L",       attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_toe_L",        attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_outerFoot_L",  attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_innerFoot_L",  attachmentGroup )



    #==============================================================================================
    # Re-organize the selection groups
    #==============================================================================================
    rigBodyGroup = rootGroup.CreateControlGroup( "RigBody" )
    rigArmsGroup = rootGroup.CreateControlGroup( "RigArms" )

    RightArmGroup = rootGroup.CreateControlGroup( "RightArm" )
    LeftArmGroup = rootGroup.CreateControlGroup( "LeftArm" )
    RightLegGroup = rootGroup.CreateControlGroup( "RightLeg" )
    LeftLegGroup = rootGroup.CreateControlGroup( "LeftLeg" )



    if num==4:
        sfmUtils.AddDagControlsToGroup( rigBodyGroup, rigRoot, rigPelvis, rigHips, rigSpine0, rigSpine1, rigSpine2, rigChest, rigNeck, rigHead )

    elif num==3:     
        sfmUtils.AddDagControlsToGroup( rigBodyGroup, rigRoot, rigPelvis, rigHips, rigSpine0, rigSpine1, rigSpine2, rigNeck, rigHead )


    elif num==2:
        sfmUtils.AddDagControlsToGroup( rigBodyGroup, rigRoot, rigPelvis, rigHips, rigSpine0, rigSpine1,rigNeck, rigHead )
    elif num==1:
        sfmUtils.AddDagControlsToGroup( rigBodyGroup, rigRoot, rigPelvis, rigHips, rigSpine0,rigNeck, rigHead )



    rigArmsGroup.AddChild( RightArmGroup )
    rigArmsGroup.AddChild( LeftArmGroup )

    if collar:
        sfmUtils.AddDagControlsToGroup( RightArmGroup,  rigHandR, rigElbowR, rigCollarR )
        sfmUtils.AddDagControlsToGroup( LeftArmGroup, rigHandL, rigElbowL, rigCollarL )
    else:

        sfmUtils.AddDagControlsToGroup( RightArmGroup,  rigHandR, rigElbowR )
        sfmUtils.AddDagControlsToGroup( LeftArmGroup, rigHandL, rigElbowL )        

    rigLegsGroup.AddChild( RightLegGroup )
    rigLegsGroup.AddChild( LeftLegGroup )

    if toe:
        sfmUtils.AddDagControlsToGroup( RightLegGroup, rigKneeR, rigFootR, rigToeR )
        sfmUtils.AddDagControlsToGroup( LeftLegGroup, rigKneeL, rigFootL, rigToeL )
    else:
        sfmUtils.AddDagControlsToGroup( RightLegGroup, rigKneeR, rigFootR )
        sfmUtils.AddDagControlsToGroup( LeftLegGroup, rigKneeL, rigFootL )        

    sfmUtils.MoveControlGroup( "rig_footRoll_L", rigLegsGroup, LeftLegGroup )
    sfmUtils.MoveControlGroup( "rig_footRoll_R", rigLegsGroup, RightLegGroup )



    sfmUtils.AddDagControlsToGroup( rigHelpersGroup, rigFootHelperR, rigFootHelperL )

    # Set the control group visiblity, this is done through the rig so it can track which
    # groups it hid, so they can be set back to being visible when the rig is detached.
    
    HideControlGroups( rig, rootGroup, "Body", "Arms", "Legs","Root" )

    #Re-order the groups

    rootGroup.MoveChildToBottom( rigBodyGroup )
    rootGroup.MoveChildToBottom( rigLegsGroup )
    rootGroup.MoveChildToBottom( rigArmsGroup )
    rootGroup.MoveChildToBottom( rootGroup.FindChildByName("Unknown",True) )





    #==============================================================================================
    # Set the selection groups colors
    #==============================================================================================
    topLevelColor = vs.Color( 0, 128, 255, 255 )
    RightColor = vs.Color( 255, 0, 0, 255 )
    LeftColor = vs.Color( 0, 255, 0, 255 )

    rigBodyGroup.SetGroupColor( topLevelColor, False )
    rigArmsGroup.SetGroupColor( topLevelColor, False )
    rigLegsGroup.SetGroupColor( topLevelColor, False )
    attachmentGroup.SetGroupColor( topLevelColor, False )
    rigHelpersGroup.SetGroupColor( topLevelColor, False )

    RightArmGroup.SetGroupColor( RightColor, False )
    LeftArmGroup.SetGroupColor( LeftColor, False )
    RightLegGroup.SetGroupColor( RightColor, False )
    LeftLegGroup.SetGroupColor( LeftColor, False )






    if (fingeropton):
        HideControlGroups(rig, rootGroup,"Fingers")
        rightFingersGroup=rootGroup.CreateControlGroup( "Right_Fingers" )
        RightArmGroup.AddChild( rightFingersGroup )
        rightFingersGroup.SetGroupColor( RightColor, False )
        rightFingersGroup.SetSelectable( True )
        for rig in rig_finger_right:
            sfmUtils.AddDagControlsToGroup(rightFingersGroup,rig)

        leftFingersGroup=rootGroup.CreateControlGroup( "Left_Fingers" )
        LeftArmGroup.AddChild( leftFingersGroup )
        leftFingersGroup.SetGroupColor( LeftColor, False )
        leftFingersGroup.SetSelectable( True )
        for rig in rig_finger_left:
            sfmUtils.AddDagControlsToGroup(leftFingersGroup,rig)        
    else:
        

        
        fingersGroup = rootGroup.FindChildByName( "Fingers", False )
        rightFingersGroup = rootGroup.FindChildByName( "RightFingers", True )
        if ( rightFingersGroup != None ):
            RightArmGroup.AddChild( rightFingersGroup )
            rightFingersGroup.SetSelectable( True )

        leftFingersGroup = rootGroup.FindChildByName( "LeftFingers", True )
        if ( leftFingersGroup != None ):
            LeftArmGroup.AddChild( leftFingersGroup )
            leftFingersGroup.SetSelectable( True )



    # End the rig definition
    sfm.EndRig()
    return

#==================================================================================================
# Script entry
#==================================================================================================


"""

        if self.sp1.isChecked() :
            spine=1
            spine1=None
            spine2=None
            spine3=None
        
        elif  self.sp2.isChecked() :
            spine=2
            spine2=None
            spine3=None

 
        elif  self.sp3.isChecked():
            spine=3
            spine3=None                
        elif  self.sp4.isChecked():
            spine=4

        if  self.toeoption.isChecked() :
            toe=True
        else:
            toe=False
            toeL=None

            toeR=None
        if  self.shoulderoption.isChecked() :
            collar=True
        else:
            collar=False
            collL=None        
            collR=None



############## #for footroll
        if self.footroll_checkbox.isChecked() :
            if self.foot_x.isChecked():
                footroll="'x'"
            elif self.foot_y.isChecked():
                footroll="'y'"
            elif self.foot_z.isChecked():                
                footroll="'z'"
		
	    elif self.foot_x.isChecked() and self.footroll_negative_checkbox.isChecked():
		    footroll="'-x'"	    
            elif self.foot_y.isChecked()and self.footroll_negative_checkbox.isChecked():
                footroll="'-y'"
            elif self.foot_z.isChecked()and self.footroll_negative_checkbox.isChecked():                
                footroll="'-z'"		
            else:
                self.error("please pick footRoll rotation Axis")
                return
            
        else:

            footroll= None
########################




        ##handpresent
            

        #if self.finger_checkBox.isChecked() :
            #if self.finger_x.isChecked():
                #handpreset="'x'"
            #elif self.finger_y.isChecked():
                #handpreset="'y'"
            #elif self.finger_z.isChecked():
                #handpreset="'z'"
            #else:
                #self.error("Please pick Finger rotation Axis")
                #return                          
        #else:
            #handpreset= None
########################

        
        if self.rig_fingers_checkbox.isChecked:
            fingerRig=True
        else:
            fingerRig=False




            

        boneList=[pelvis,spine0,spine1,spine2,spine3,neck,head,uplegR,lowlegR,footR,toeR,collR,uparmR,lowarmR,handR,uplegL,lowlegL,footL,toeL,collL,uparmL,lowarmL,handL]
        
        #creates script based on  #of spine & toe bones and collar bones
        
        try:

            fob=open("platform\\scripts\\sfm\\animset\\" + name,"w")
            fob.write(script+"\nboneList= %s \nBuildRig(%s,%s,%s,boneList,%s,%s,%s);" %(boneList,spine,toe,collar,footroll,fingerRig,None))
            fob.close()

     


                
            self.Message("file '"+ name + "' was created and saved in\n 'game\\platform\\scripts\\sfm\\animset\\'")
            

        except  IOError as e:

            self.error(e)


        except  UnicodeEncodeError as e:
            self.error(e)


        except  WindowsError as e:
            self.error(e)




#==================================================================================================
# ui setup
#==================================================================================================




    def setupUi(self, window):
        

        window.setObjectName("window")
        window.resize(929, 455)
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("platform/tools/images/sfm/sfm_app.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        #window.setWindowIcon(icon)
        self.gridLayout_4 = QtGui.QGridLayout(window)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtGui.QGroupBox(window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(561, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(42)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtGui.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)




        
        self.bone_upperlegL = QtGui.QComboBox(self.groupBox_2)
        self.bone_upperlegL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_upperlegL.setObjectName("bone_upperlegL")

        self.bone_upperlegL.setMaxVisibleItems(30)

        self.gridLayout.addWidget(self.bone_upperlegL, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 2, 1, 1)
        self.bone_collarL = QtGui.QComboBox(self.groupBox_2)
        self.bone_collarL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_collarL.setObjectName("bone_collarL")
        self.bone_collarL.setMaxVisibleItems(30)

        self.gridLayout.addWidget(self.bone_collarL, 0, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.bone_lowerlegL = QtGui.QComboBox(self.groupBox_2)
        self.bone_lowerlegL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_lowerlegL.setObjectName("bone_lowerlegL")
        self.bone_lowerlegL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_lowerlegL, 1, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 2, 1, 1)
        self.bone_upperarmL = QtGui.QComboBox(self.groupBox_2)
        self.bone_upperarmL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_upperarmL.setObjectName("bone_upperarmL")
        self.bone_upperarmL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_upperarmL, 1, 3, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.bone_footL = QtGui.QComboBox(self.groupBox_2)
        self.bone_footL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_footL.setObjectName("bone_footL")
        self.bone_footL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_footL, 2, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 2, 1, 1)
        self.bone_lowerarmL = QtGui.QComboBox(self.groupBox_2)
        self.bone_lowerarmL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_lowerarmL.setObjectName("bone_lowerarmL")
        self.bone_lowerarmL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_lowerarmL, 2, 3, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)
        self.bone_toeL = QtGui.QComboBox(self.groupBox_2)
        self.bone_toeL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_toeL.setObjectName("bone_toeL")
        self.bone_toeL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_toeL, 3, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 2, 1, 1)
        self.bone_handL = QtGui.QComboBox(self.groupBox_2)
        self.bone_handL.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_handL.setObjectName("bone_handL")
        self.bone_handL.setMaxVisibleItems(30)
        self.gridLayout.addWidget(self.bone_handL, 3, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(window)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(42)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 2, 1, 1)
        self.upperarmR = QtGui.QComboBox(self.groupBox_3)
        self.upperarmR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.upperarmR.setObjectName("upperarmR")
        self.upperarmR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.upperarmR, 1, 3, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.bone_upperlegR = QtGui.QComboBox(self.groupBox_3)
        self.bone_upperlegR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_upperlegR.setObjectName("bone_upperlegR")
        self.bone_upperlegR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_upperlegR, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.bone_collarR = QtGui.QComboBox(self.groupBox_3)
        self.bone_collarR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_collarR.setObjectName("bone_collarR")
        self.bone_collarR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_collarR, 0, 3, 1, 1)
        self.bone_footR = QtGui.QComboBox(self.groupBox_3)
        self.bone_footR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_footR.setObjectName("bone_footR")
        self.bone_footR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_footR, 2, 1, 1, 1)
        self.handR = QtGui.QComboBox(self.groupBox_3)
        self.handR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.handR.setObjectName("handR")
        self.handR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.handR, 3, 3, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 2, 1, 1)
        self.bone_toeR = QtGui.QComboBox(self.groupBox_3)
        self.bone_toeR.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bone_toeR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_toeR.setObjectName("bone_toeR")
        self.bone_toeR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_toeR, 3, 1, 1, 1)
        self.bone_lowerlegR = QtGui.QComboBox(self.groupBox_3)
	
        self.bone_lowerlegR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_lowerlegR.setObjectName("bone_lowerlegR")
        self.bone_lowerlegR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_lowerlegR, 1, 1, 1, 1)
        self.bone_lowerarmR = QtGui.QComboBox(self.groupBox_3)
        self.bone_lowerarmR.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_lowerarmR.setObjectName("bone_lowerarmR")
        self.bone_lowerarmR.setMaxVisibleItems(30)
        self.gridLayout_2.addWidget(self.bone_lowerarmR, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(window)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(50, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 4, 1, 1)
        self.bone_spine2 = QtGui.QComboBox(self.groupBox)
        self.bone_spine2.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_spine2.setObjectName("bone_spine2")
        self.bone_spine2.setMaxVisibleItems(30)
        self.gridLayout_3.addWidget(self.bone_spine2, 0, 8, 2, 1)
        self.bone_spine1 = QtGui.QComboBox(self.groupBox)
        self.bone_spine1.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_spine1.setObjectName("bone_spine1")
        self.bone_spine1.setMaxVisibleItems(30)
        self.gridLayout_3.addWidget(self.bone_spine1, 2, 5, 2, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 6, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 6, 1, 1)
        self.bone_spine3 = QtGui.QComboBox(self.groupBox)
        self.bone_spine3.setEnabled(True)
        self.bone_spine3.setAcceptDrops(False)
        self.bone_spine3.setEditable(False)
        self.bone_spine3.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.bone_spine3.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_spine3.setObjectName("bone_spine3")
        self.bone_spine3.setMaxVisibleItems(30)
        self.gridLayout_3.addWidget(self.bone_spine3, 2, 8, 2, 1)
        self.sp4 = QtGui.QRadioButton(self.groupBox)
        self.sp4.setChecked(True)
        self.sp4.setObjectName("sp4")
        self.gridLayout_3.addWidget(self.sp4, 0, 0, 1, 1)
        
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)
        
        self.bone_spine0 = QtGui.QComboBox(self.groupBox)
        self.bone_spine0.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_spine0.setObjectName("bone_spine0")
        self.bone_spine0.setMaxVisibleItems(30)
       # self.bone_spine0.setFont(font)
        self.gridLayout_3.addWidget(self.bone_spine0, 0, 5, 2, 1)
        
        self.sp2 = QtGui.QRadioButton(self.groupBox)
        self.sp2.setObjectName("sp2")
        
        self.gridLayout_3.addWidget(self.sp2, 0, 2, 1, 1)
        
        self.sp1 = QtGui.QRadioButton(self.groupBox)
        self.sp1.setObjectName("sp1")
        self.gridLayout_3.addWidget(self.sp1, 0, 3, 1, 1)
        
        self.sp3 = QtGui.QRadioButton(self.groupBox)
        self.sp3.setObjectName("sp3")
        self.gridLayout_3.addWidget(self.sp3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 2, 0, 1, 2)
        self.createfile = QtGui.QToolButton(window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createfile.sizePolicy().hasHeightForWidth())
        self.createfile.setSizePolicy(sizePolicy)
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.createfile.setFont(font2)
	

	
        self.createfile.setAutoFillBackground(False)
        self.createfile.setCheckable(False)
        self.createfile.setChecked(False)
        self.createfile.setObjectName("createfile")
        self.gridLayout_4.addWidget(self.createfile, 7, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 20, 120, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(window)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bone_head = QtGui.QComboBox(window)
        self.bone_head.setEnabled(True)
        self.bone_head.setMouseTracking(True)
        self.bone_head.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bone_head.setAcceptDrops(True)
        self.bone_head.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.bone_head.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_head.setDuplicatesEnabled(False)
        self.bone_head.setObjectName("bone_head")
        self.bone_head.setMaxVisibleItems(30)
        self.horizontalLayout.addWidget(self.bone_head)
        self.label_3 = QtGui.QLabel(window)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bone_neck = QtGui.QComboBox(window)
        self.bone_neck.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_neck.setObjectName("bone_neck")
        self.bone_neck.setMaxVisibleItems(30)
        self.horizontalLayout.addWidget(self.bone_neck)
        self.label_2 = QtGui.QLabel(window)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bone_pelvis = QtGui.QComboBox(window)
        self.bone_pelvis.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bone_pelvis.setObjectName("bone_pelvis")
        self.bone_pelvis.setMaxVisibleItems(30)
        self.horizontalLayout.addWidget(self.bone_pelvis)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(window)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(120, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.toeoption = QtGui.QCheckBox(self.groupBox_4)
        self.toeoption.setEnabled(True)
        self.toeoption.setChecked(True)
        self.toeoption.setObjectName("toeoption")
        self.horizontalLayout_2.addWidget(self.toeoption)
        self.gridLayout_4.addWidget(self.groupBox_4, 5, 0, 1, 2)
        self.shoulderoption = QtGui.QCheckBox(self.groupBox_4)
        self.shoulderoption.setEnabled(True)
        self.shoulderoption.setChecked(True)
        self.shoulderoption.setObjectName("shoulderoption")
        self.horizontalLayout_2.addWidget(self.shoulderoption)

        self.line_2 = QtGui.QFrame(self.groupBox_4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.footroll_checkbox = QtGui.QCheckBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footroll_checkbox.sizePolicy().hasHeightForWidth())
        self.footroll_checkbox.setSizePolicy(sizePolicy)
        self.footroll_checkbox.setObjectName("footroll_checkbox")
        self.horizontalLayout_2.addWidget(self.footroll_checkbox)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
	
	
	self.footroll_negative_checkbox = QtGui.QCheckBox(self.groupBox_4)
	self.footroll_negative_checkbox.setEnabled(False)
	
	
	
	
	
	self.horizontalLayout_2.addWidget(self.footroll_negative_checkbox)
        self.horizontalLayout_2.addWidget(self.label_4)
        self.frame = QtGui.QFrame(self.groupBox_4)
        self.frame.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.foot_x = QtGui.QRadioButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foot_x.sizePolicy().hasHeightForWidth())
        self.foot_x.setSizePolicy(sizePolicy)
        self.foot_x.setMinimumSize(QtCore.QSize(35, 5))
        self.foot_x.setMaximumSize(QtCore.QSize(30, 30))
        self.foot_x.setWhatsThis("")
        self.foot_x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.foot_x.setAutoFillBackground(False)
        self.foot_x.setChecked(False)
        self.foot_x.setAutoRepeat(False)
        self.foot_x.setObjectName("foot_x")
        self.horizontalLayout_3.addWidget(self.foot_x)
        self.foot_y = QtGui.QRadioButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foot_y.sizePolicy().hasHeightForWidth())
        self.foot_y.setSizePolicy(sizePolicy)
        self.foot_y.setMaximumSize(QtCore.QSize(30, 16777215))
        self.foot_y.setAutoRepeat(False)
        self.foot_y.setObjectName("foot_y")
        self.horizontalLayout_3.addWidget(self.foot_y)
        self.foot_z = QtGui.QRadioButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foot_z.sizePolicy().hasHeightForWidth())
        self.foot_z.setSizePolicy(sizePolicy)
        self.foot_z.setMaximumSize(QtCore.QSize(30, 30))
        self.foot_z.setObjectName("foot_z")
        self.horizontalLayout_3.addWidget(self.foot_z)
        self.horizontalLayout_2.addWidget(self.frame)
        self.line = QtGui.QFrame(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 30))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.rig_fingers_checkbox = QtGui.QCheckBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rig_fingers_checkbox.sizePolicy().hasHeightForWidth())
        self.rig_fingers_checkbox.setSizePolicy(sizePolicy)
        self.rig_fingers_checkbox.setObjectName("rig_fingers_Button")
        self.horizontalLayout_2.addWidget(self.rig_fingers_checkbox)
        self.finger_checkBox = QtGui.QCheckBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finger_checkBox.sizePolicy().hasHeightForWidth())
        self.finger_checkBox.setSizePolicy(sizePolicy)
        self.finger_checkBox.setObjectName("finger_checkBox")
        self.finger_checkBox.hide()
        self.horizontalLayout_2.addWidget(self.finger_checkBox)
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        self.label_25.hide()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.label_25.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.label_25)
        self.frame_2 = QtGui.QFrame(self.groupBox_4)
        self.frame_2.setEnabled(False)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.finger_x = QtGui.QRadioButton(self.frame_2)
        self.finger_x.hide()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finger_x.sizePolicy().hasHeightForWidth())
        self.finger_x.setSizePolicy(sizePolicy)
        self.finger_x.setMinimumSize(QtCore.QSize(30, 5))
        self.finger_x.setMaximumSize(QtCore.QSize(30, 30))
        self.finger_x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.finger_x.setAutoFillBackground(False)
        self.finger_x.setChecked(False)
        self.finger_x.setAutoRepeat(False)
        self.finger_x.setAutoExclusive(True)
        self.finger_x.setObjectName("finger_x")
        self.horizontalLayout_4.addWidget(self.finger_x)
        self.finger_y = QtGui.QRadioButton(self.frame_2)
        self.finger_y.hide()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finger_y.sizePolicy().hasHeightForWidth())
        self.finger_y.setSizePolicy(sizePolicy)
        self.finger_y.setMaximumSize(QtCore.QSize(30, 16777215))
        self.finger_y.setAutoRepeat(True)
        self.finger_y.setObjectName("finger_y")
        self.horizontalLayout_4.addWidget(self.finger_y)
        self.finger_z = QtGui.QRadioButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finger_z.sizePolicy().hasHeightForWidth())
        self.finger_z.setSizePolicy(sizePolicy)
        self.finger_z.setMaximumSize(QtCore.QSize(30, 30))
        self.finger_z.setAutoRepeat(True)
        self.finger_z.setObjectName("finger_z")
        self.finger_z.hide()
        self.horizontalLayout_4.addWidget(self.finger_z)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout_4.addWidget(self.groupBox_4, 5, 0, 1, 2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createfile.sizePolicy().hasHeightForWidth())
        self.openfile = QtGui.QToolButton(window)

        self.openfile.setSizePolicy(sizePolicy)

        self.openfile.setFont(font)
        self.openfile.setAutoFillBackground(False)
        self.openfile.setCheckable(False)
        self.openfile.setChecked(False)
        self.openfile.setObjectName("createfile")
        self.gridLayout_4.addWidget(self.openfile, 6, 0, 1, 2)
	
	font2.setPointSize(10)
	self.groupBox_2.setFont(font2)
	self.groupBox_3.setFont(font2)
	self.groupBox.setFont(font2)
	self.groupBox_4.setFont(font2)

        ##finds bones adds to lists
	self.bonename_to_obj={}
	
        count=0
        global bonelist
        tmpDag="null"
        
        while(tmpDag != None ):
            tmpDag = sfm.NextSelectedDag()
            if tmpDag == None:
                break
            b=str(tmpDag).find('(')
            e=str(tmpDag).find(')')
            bonename=str(tmpDag)[b+1:e]
            if "dme" in bonename.lower() :
                continue
	    self.bonename_to_obj[bonename]=tmpDag
            bonelist.append(bonename)
            


         #sorts alphabetically  
        bonelist.sort()
        for bonename in bonelist:#adds bones to each drop down list
            #ignores fingers
            if "finger" in bonename.lower() :
                continue
            self.bone_head.addItem("")
            self.bone_head.setItemText(count,QtGui.QApplication.translate("window", bonename, None, QtGui.QApplication.UnicodeUTF8))
            self.bone_footL.addItem(bonename)
            self.bone_footR.addItem(bonename)
            self.bone_spine0.addItem(bonename)
            self.bone_spine1.addItem(bonename)
            self.bone_spine2.addItem(bonename)
            self.bone_spine3.addItem(bonename)
            self.bone_neck.addItem(bonename)
            self.bone_lowerarmL.addItem(bonename)
            self.bone_lowerarmR.addItem(bonename)
            self.bone_upperarmL.addItem(bonename)
            self.upperarmR.addItem(bonename)
            self.bone_pelvis.addItem(bonename)
            self.bone_upperlegR.addItem(bonename)
            self.bone_upperlegL.addItem(bonename)
            self.bone_lowerlegR.addItem(bonename)
            self.bone_lowerlegL.addItem(bonename)
            self.bone_toeR.addItem(bonename)
            self.bone_toeL.addItem(bonename)
            self.handR.addItem(bonename)
            self.bone_handL.addItem(bonename)
            self.bone_collarR.addItem(bonename)
            self.bone_collarL.addItem(bonename)
            count+=1


        QtCore.QObject.connect(self.footroll_checkbox, QtCore.SIGNAL("toggled(bool)"), self.frame.setEnabled)
        QtCore.QObject.connect(self.finger_checkBox, QtCore.SIGNAL("toggled(bool)"), self.frame_2.setEnabled)
        QtCore.QObject.connect(self.footroll_checkbox, QtCore.SIGNAL("toggled(bool)"), self.label_4.setEnabled)
        QtCore.QObject.connect(self.finger_checkBox, QtCore.SIGNAL("toggled(bool)"), self.label_25.setEnabled)
	QtCore.QObject.connect(self.footroll_checkbox, QtCore.SIGNAL("toggled(bool)"), self.footroll_negative_checkbox.setEnabled)
	
	
	#for autofind
	self.label_16.setEnabled(False)
	self.label_22.setEnabled(False)
	self.label_23.setEnabled(False)
	self.label_21.setEnabled(False)
	self.label_24.setEnabled(False)
	self.label_9.setEnabled(False)
	self.label_14.setEnabled(False)
	self.label_10.setEnabled(False)	
	
	
	self.bone_lowerlegR.setEnabled(False)
	self.bone_upperlegL.setEnabled(False)
	self.bone_lowerarmL.setEnabled(False)
	self.bone_upperarmL.setEnabled(False)
	self.bone_lowerarmR.setEnabled(False)
	self.upperarmR.setEnabled(False)
	self.bone_lowerlegL.setEnabled(False)
	self.bone_upperlegR.setEnabled(False)
	
	
	self.bone_handL.currentIndexChanged.connect(lambda: self.autofind(self.bone_handL,self.bone_lowerarmL,self.bone_upperarmL))
	self.handR.currentIndexChanged.connect(lambda: self.autofind(self.handR,self.bone_lowerarmR,self.upperarmR))	
	self.bone_footL.currentIndexChanged.connect(lambda: self.autofind(self.bone_footL,self.bone_lowerlegL,self.bone_upperlegL))	
	self.bone_footR.currentIndexChanged.connect(lambda: self.autofind(self.bone_footR,self.bone_lowerlegR,self.bone_upperlegR))
	##
	
	
	
	
        
        self.retranslateUi(window)


        QtCore.QMetaObject.connectSlotsByName(window)
        #create file when clicked
        self.createfile.clicked.connect(lambda: self.main())
        try:
            self.openfile.clicked.connect(lambda: self.opensave())
        except IOError as e:
            self.error("There was an error opening the file",e)
        #hides unused  bones
        self.sp1.clicked.connect(lambda: self.hide())
        self.sp2.clicked.connect(lambda: self.hide())
        self.sp3.clicked.connect(lambda: self.hide())
        self.sp4.clicked.connect(lambda: self.hide())
        self.toeoption.clicked.connect(lambda: self.hide())
        self.shoulderoption.clicked.connect(lambda: self.hide())
        #self.rig_fingers_checkbox.clicked.connect(lambda: self.rigfingers())
        #calls auto find method
        self.find(bonelist)


        
#creates ui
    def retranslateUi(self, window):
        window.setWindowTitle(QtGui.QApplication.translate("window", "Auto-Rigger V1.9", None, QtGui.QApplication.UnicodeUTF8))

        self.groupBox_2.setTitle(QtGui.QApplication.translate("window", "Left-side", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneUpperLegL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneCollarL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneLowerlegL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneupperArmL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneFootL</p></body></html>	", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneLowerArmL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneToeL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneHandL</p></body></html>	", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("window", "Right-side", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneFootR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneUpperLegR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneLowerArmR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneCollarR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneToeR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneLowerLegR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneUpperArmR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">boneHandR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("window", "misc option", None, QtGui.QApplication.UnicodeUTF8))
        self.toeoption.setText(QtGui.QApplication.translate("window", "use toe bones", None, QtGui.QApplication.UnicodeUTF8))
        self.shoulderoption.setText(QtGui.QApplication.translate("window", "use collar bones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("window", "Spine Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">spine1</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">spine3</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">spine2</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sp4.setText(QtGui.QApplication.translate("window", "4 spine bones", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">spine0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sp2.setText(QtGui.QApplication.translate("window", "2 spine bones", None, QtGui.QApplication.UnicodeUTF8))
        self.sp3.setText(QtGui.QApplication.translate("window", "3 spine bones", None, QtGui.QApplication.UnicodeUTF8))
        #self.cfg.setToolTip(QtGui.QApplication.translate("window", "Creates a text file that SFM uses to organizes\nyour models control groups", None, QtGui.QApplication.UnicodeUTF8))
        #self.cfg.setText(QtGui.QApplication.translate("window", "create animation groups", None, QtGui.QApplication.UnicodeUTF8))
        #self.createfile.setWhatsThis(QtGui.QApplication.translate("window", "<html><head/><body><p><span style=\" font-size:2pt;\">fh</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.createfile.setText(QtGui.QApplication.translate("window", "Create Script", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">Head</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\">Neck</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("window", "<html><head/><body><p align=\"right\" >Pelvis</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.openfile.setText(QtGui.QApplication.translate("window", "Load Rig Script", None, QtGui.QApplication.UnicodeUTF8))
        self.footroll_checkbox.setToolTip(QtGui.QApplication.translate("window", "<html><head/><body><p>creates a channel to make posing foot for walking easier.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.footroll_checkbox.setText(QtGui.QApplication.translate("window", "add footroll", None, QtGui.QApplication.UnicodeUTF8))
	
	
	self.footroll_negative_checkbox.setText(QtGui.QApplication.translate("window", "Negative value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("window", "foot Axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_x.setToolTip(QtGui.QApplication.translate("window", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_x.setText(QtGui.QApplication.translate("window", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_y.setToolTip(QtGui.QApplication.translate("window", "green", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_y.setText(QtGui.QApplication.translate("window", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_z.setToolTip(QtGui.QApplication.translate("window", "blue", None, QtGui.QApplication.UnicodeUTF8))
        self.foot_z.setText(QtGui.QApplication.translate("window", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.rig_fingers_checkbox.setToolTip(QtGui.QApplication.translate("window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-align:center;\">makes fingers not lag</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rig_fingers_checkbox.setText(QtGui.QApplication.translate("window", "rig fingers", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_checkBox.setToolTip(QtGui.QApplication.translate("window", "adds fist and open palm presets to fingers", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_checkBox.setText(QtGui.QApplication.translate("window", "Add finger presets", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("window", "Finger Axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_x.setToolTip(QtGui.QApplication.translate("window", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_x.setText(QtGui.QApplication.translate("window", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_y.setToolTip(QtGui.QApplication.translate("window", "green", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_y.setText(QtGui.QApplication.translate("window", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_z.setToolTip(QtGui.QApplication.translate("window", "blue", None, QtGui.QApplication.UnicodeUTF8))
        self.finger_z.setText(QtGui.QApplication.translate("window", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.sp1.setText(QtGui.QApplication.translate("window", "1 spine bone", None, QtGui.QApplication.UnicodeUTF8))

#==================================================================================================
# Script entry
#==================================================================================================

if __name__ == "__main__":
    

    window = QtGui.QWidget()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()


