# import os
import time
import xml.dom.minidom
import pathlib

DAC_CONTEST = pathlib.Path('/home/xilinx/jupyter_notebooks/dac_sdc_2020/')
IMG_DIR = DAC_CONTEST / 'images'
RESULT_DIR = DAC_CONTEST / 'result'
    

# Return a batch of image dir  when `send` is called
class Team:
    def __init__(self, teamname, batch_size):
        # self.dac_contest = DAC_CONTEST
        # self.img_dir = IMG_DIR                
        # self.result_path = RESULT_DIR        
        self._result_path = RESULT_DIR / teamname
        self.team_dir = DAC_CONTEST / teamname      
        self.batch_size = batch_size  

        folder_list = [self.team_dir, self._result_path]
        for folder in folder_list:
            if not folder.is_dir():
                folder.mkdir()
        
        self.img_list = self.get_image_paths()
        self.batch_count = 0

    def get_image_paths(self):
        names_temp = [f for f in IMG_DIR.iterdir() if f.suffix == '.jpg']
        names_temp.sort(key= lambda x:int(x.stem))
        return names_temp

    # Returns list of images paths for next batch of images
    def get_next_batch(self):
        start_idx = self.batch_count * self.batch_size
        self.batch_count += 1
        end_idx = self.batch_count * self.batch_size

        if start_idx >= len(self.img_list):
            return None
        elif end_idx > len(self.img_list):
            return self.img_list[start_idx:]
        else:
            return self.img_list[start_idx:end_idx]

    def get_bitstream_path(self):
        return str(self.team_dir / "dac_sdc.bit")
    
    def reset_batch_count(self):
        self.batch_count = 0
    
    def save_results_xml(self, result_rectangle, runtime, energy):
        if len(result_rectangle) != len(self.img_list):
            raise ValueError("Result length not equal to number of images.")

        doc = xml.dom.minidom.Document()
        root = doc.createElement('results')

        perf_e = doc.createElement('performance')
        
        # Runtime
        runtime_e = doc.createElement('runtime')
        runtime_e.appendChild(doc.createTextNode(str(runtime)))
        perf_e.appendChild(runtime_e)
        root.appendChild(runtime_e)

        # Energy
        energy_e = doc.createElement('energy')
        energy_e.appendChild(doc.createTextNode(str(energy)))
        perf_e.appendChild(energy_e)
        root.appendChild(energy_e)


        for i in range(len(self.img_list)):
            image_e = root.appendChild(doc.createElement("image"))

            doc.appendChild(root)
            name_e = doc.createElement('filename')
            name_t = doc.createTextNode(self.img_list[i].name)
            name_e.appendChild(name_t)
            image_e.appendChild(name_e)

            size_e = doc.createElement('size')
            node_width = doc.createElement('width')
            node_width.appendChild(doc.createTextNode("640"))
            node_length = doc.createElement('length')
            node_length.appendChild(doc.createTextNode("360"))
            size_e.appendChild(node_width)
            size_e.appendChild(node_length)
            image_e.appendChild(size_e)

            object_node = doc.createElement('object')
            node_bnd_box = doc.createElement('bndbox')
            node_bnd_box_xmin = doc.createElement('xmin')
            node_bnd_box_xmin.appendChild(
                doc.createTextNode(str(result_rectangle[i][0])))
            node_bnd_box_xmax = doc.createElement('xmax')
            node_bnd_box_xmax.appendChild(
                doc.createTextNode(str(result_rectangle[i][1])))
            node_bnd_box_ymin = doc.createElement('ymin')
            node_bnd_box_ymin.appendChild(
                doc.createTextNode(str(result_rectangle[i][2])))
            node_bnd_box_ymax = doc.createElement('ymax')
            node_bnd_box_ymax.appendChild(
                doc.createTextNode(str(result_rectangle[i][3])))
            node_bnd_box.appendChild(node_bnd_box_xmin)
            node_bnd_box.appendChild(node_bnd_box_xmax)
            node_bnd_box.appendChild(node_bnd_box_ymin)
            node_bnd_box.appendChild(node_bnd_box_ymax)

            object_node.appendChild(node_bnd_box)
            image_e.appendChild(object_node)

        file_name = self._result_path / "results.xml"
        with open(file_name, 'w') as fp:
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
