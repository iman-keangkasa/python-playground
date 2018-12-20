'''
A robot class:
    todo:
    [ ] xml parser for parsing different robot 
        characteristics
    [ ] develop two types of robot: industrial
        and mobile
    [ ] using quaternion approach to solve
        inverse kinematics and dynamics
    [ ] making sure that the xml for robot
        is compatible with gazebo and URDF for
        ROS
    
                THE ROBOT
    TYPE:
    [ ] Option between manipulator or mobile
    [ ] mobile use 2D(R**2 + S**1) motion or 3D motion (R**3 + S**3)
        R is a the positional space and S is the orientation space
    
    JOINT:
    [ ] Revolute joint should have access to:
        [ ] Position on each link if it were a serial/manipulator robot
        [ ] joint type (revolute or prismatic)
            The option of free would set 6 dof for mobile robot?
        [ ] joint angle
        [ ] a and alpha (DH parameter)
        [ ] the choice of DH standard or modified
        [ ] joint limit
        [ ] link inertia matrix
        [ ] link centre of gravity
        [ ] link mass
        [ ] motor gear ratio
        [ ] joint friction (from motor)
        [ ] motor inertia (from motor) try its CAD?
        [ ] coulomb friction
        [ ] can take in symbolic variables

    LINK
        Mobile robot:
        [ ] for mobile robot, imaginary that change
            in length and orientation
        Manipulator:
        [ ] Will have characteristic defined by joints
        [ ] Rigid or non-rigid (for small flexibility allowance?)
        [ ] Origin will be joint that attached to the previous link
        [ ] 
    POSITION
        Mobile robot:
        [ ] based on deterministic model, the state of the robot is
            handled by the state object
        
        
        Manipulator:
        [ ] Provide the deterministic model, which are the forward 
            kinematics and the inverse kinematic model of the robot

    DYNAMICS
        Mobile robot:
        [ ] Deterministic model based on Newton's second law

        Articulate robot:
        [ ] Jacobian
        [ ] Acc constraint motion,
        [ ] Kinodynamic motion
        [ ] non-holonimic motion for end effector



'''
