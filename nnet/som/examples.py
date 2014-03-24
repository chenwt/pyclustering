from nnet.som import som;
from nnet.som import type_conn;
from nnet.som import type_init;

from samples.definitions import SIMPLE_SAMPLES;
from samples.definitions import FCPS_SAMPLES;

from support import read_sample;

def template_self_organization(file, rows, cols, time, structure, init_type = type_init.uniform_grid):
    sample = read_sample(file);
    network = som(rows, cols, sample, time, structure, init_type);
    network.train();
    network.show_network(False, dataset = False);

def som_sample1():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 2, 100, type_conn.grid_four);
    
def som_sample2():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 3, 100, type_conn.grid_four);
    
def som_sample3():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 2, 2, 100, type_conn.grid_four);
    
def som_sample4():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, 5, 100, type_conn.grid_four);
    
def som_sample5():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 2, 2, 100, type_conn.grid_four);
    
def som_lsun():
    template_self_organization(FCPS_SAMPLES.SAMPLE_LSUN, 5, 5, 100, type_conn.grid_four);
    
def som_target():
    template_self_organization(FCPS_SAMPLES.SAMPLE_TARGET, 5, 5, 100, type_conn.grid_four);
    
def som_tetra():
    template_self_organization(FCPS_SAMPLES.SAMPLE_TETRA, 1, 4, 100, type_conn.grid_four);
    
def som_two_diamonds():
    template_self_organization(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 5, 5, 100, type_conn.grid_four);
    
def som_elongate():
    template_self_organization(SIMPLE_SAMPLES.SAMPLE_ELONGATE, 5, 5, 100, type_conn.grid_four);
    
def som_wing_nut():
    template_self_organization(FCPS_SAMPLES.SAMPLE_WING_NUT, 5, 5, 100, type_conn.grid_four);
    
def som_chainlink():
    template_self_organization(FCPS_SAMPLES.SAMPLE_CHAINLINK, 5, 5, 100, type_conn.grid_four);
    
def som_atom():
    template_self_organization(FCPS_SAMPLES.SAMPLE_ATOM, 5, 5, 100, type_conn.grid_four);
    
def som_golf_ball():
    template_self_organization(FCPS_SAMPLES.SAMPLE_GOLF_BALL, 5, 5, 100, type_conn.grid_four);
    
def som_hepta():
    template_self_organization(FCPS_SAMPLES.SAMPLE_HEPTA, 1, 7, 100, type_conn.grid_four);
    
def som_engy_time():
    template_self_organization(FCPS_SAMPLES.SAMPLE_ENGY_TIME, 5, 5, 100, type_conn.grid_four);
    
def som_target_diffence_intialization():
    template_self_organization(FCPS_SAMPLES.SAMPLE_TARGET, 9, 9, 150, type_conn.grid_four, type_init.random_centroid);
    template_self_organization(FCPS_SAMPLES.SAMPLE_TARGET, 9, 9, 150, type_conn.grid_four, type_init.random_surface);
    template_self_organization(FCPS_SAMPLES.SAMPLE_TARGET, 9, 9, 150, type_conn.grid_four, type_init.uniform_grid);
    
def som_two_diamonds_diffence_intialization():
    template_self_organization(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 5, 5, 150, type_conn.grid_four, type_init.random_centroid);
    template_self_organization(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 5, 5, 150, type_conn.grid_four, type_init.random_surface);
    template_self_organization(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 5, 5, 150, type_conn.grid_four, type_init.uniform_grid);    


som_sample1();
som_sample2();
som_sample3();
som_sample4();
som_sample5();
som_lsun();
som_target();
som_tetra();
som_two_diamonds();
som_elongate();
som_wing_nut();
som_chainlink();
som_atom();
som_golf_ball();
som_hepta();
som_engy_time();

#som_target_diffence_intialization();
#som_two_diamonds_diffence_intialization();