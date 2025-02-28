import os

class dataset_class:

    def __init__(self, required_no):
        # required_no is the argument, which tells us the minium requirement for
        # training image.

        #Dataset Name
        self.dir = ("images/ORL")

        # Train-Images
        self.images_name_for_train = [] # the image path's for training. All the image which we are going to use for training are stored in this array.
        self.target_name_as_array= [] # this will store only names of the person which we are using for training.
        self.target_name_as_set = {} # this will store the label-no's, what is that person. For that label, who is the person. That is stored here.
        self.y_for_train = [] # images_name_for_train, here we have a vector of all path's which we wish to train. So each path, what is the label of that path is stored here.

        # The label-tells us what is the allocated-number to the person. using the number we can identify who the person is
        # the target-label, has the above images name
        self.no_of_elements_for_train = [] # for each label how much image Are store

        # Test-Images.
        self.images_name_for_test = []
        self.y_for_test = []
        self.no_of_elements_for_test = []


        per_no = 0 #label for the person's
        for name in os.listdir(self.dir):
            dir_path = os.path.join(self.dir, name)
            if os.path.isdir(dir_path):
                if len(os.listdir(dir_path)) >= required_no:
                    i = 0 #count of how much images from that folder are stored.
                    for img_name in os.listdir(dir_path):
                        img_path = os.path.join(dir_path, img_name)
                        if i < required_no:
                            self.images_name_for_train += [img_path]
                            self.y_for_train += [per_no]

                             # for that label how much images are there for tarining,
                            # no_of_elements_for_train this array will
                            # store how much tarining images is stored for that
                            #person(label
                            if len(self.no_of_elements_for_train) > per_no:
                                self.no_of_elements_for_train[per_no] += 1
                            else:
                                self.no_of_elements_for_train += [1]

                            if i is 0:
                                self.target_name_as_array += [name] #name of the person
                                #actuall name is stored
                                self.target_name_as_set[per_no] = name

                        else:
                            self.images_name_for_test += [img_path]
                            self.y_for_test += [per_no]
                            if len(self.no_of_elements_for_test) > per_no:
                                self.no_of_elements_for_test[per_no] += 1
                            else:
                                self.no_of_elements_for_test += [1]
                        i += 1
                    per_no += 1