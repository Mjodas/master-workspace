# Base imports
import os
import argparse
from pathlib import Path

# Third party imports
import pandas as pd

# Custom imports
from lpi_modulations.barker import Barker

# Modulations
modulations = {
    'BRK': Barker,
    'FMCW':'FMCW',
    'POLYPHASE':'POLYPHASE'
}

# Modulation types 
modulation_types = modulations.keys()

# Arguments
parser = argparse.ArgumentParser()

# Mandatory arguments
parser.add_argument("mod", help="Choose modulation type", type=str, choices=modulation_types)
parser.add_argument("snr", help="Signal to noise ratio", type=int)
parser.add_argument("n_samples", help="Number of samples", type=int)
parser.add_argument("noise_samples", help="For every sample, create a sample with only noise", type=bool)

# Optional arguments
parser.add_argument("--verbosity", help="Increase output verbosity", type=bool)

args = parser.parse_args()

# Default directories
data_dir = 'data/'
snr_dir = 'snr{}/'.format(args.snr)
mod_dir = '{}/'.format(args.mod)
path = data_dir+snr_dir+mod_dir

# Store random generated noise at snr level x
random_noise_dir = 'noise/'

# Store signal with and without noise, good for visual inspection
signals_with_noise_dir = 'signals_with_noise/'
signals_without_noise_dir = 'signals_without_noise/'

# Default filenames
master_metadata_filename = 'master_metadata.csv'
metadata_filename = 'metadata.csv'

# If needed, create main data directory and directories for snr level and modulation
Path(data_dir).mkdir(parents=True, exist_ok=True)
Path(path).mkdir(parents=True, exist_ok=True)
Path(path + random_noise_dir).mkdir(parents=True, exist_ok=True)
Path(path + signals_with_noise_dir).mkdir(parents=True, exist_ok=True)
Path(path + signals_without_noise_dir).mkdir(parents=True, exist_ok=True)

# Meta data columns
cols = ['filename', 'modulation_type', 'snr', 'lpi', 'sample_frequency']

# Master metadata file
if os.path.exists(data_dir + master_metadata_filename):
    # Read master metadata file
    master_metadata = pd.read_csv(data_dir+master_metadata_filename)
else:
    # Create metadata file
    master_metadata = pd.DataFrame(columns=cols)


# Metadata file for modulation type at specific snr
if os.path.exists(path+metadata_filename):
    # Read metadata file
    metadata = pd.read_csv(path+metadata_filename)
else:
    # Create metadata file
    metadata = pd.DataFrame(columns=cols)

# Number of available spectrograms at snr x and modulation type y.
base_index = metadata.shape[0]

# Get modulation 
modulation = modulations[args.mod]

# Generate and save n randomized samples
for index in range(args.n_samples):

    # Adjust index for correct naming
    i = index + base_index

    # Generate data
    #s_i, s_q, modulation_vector = modulation.generate_random_sample()

    # Add Noise
    #s_i_wgn = add_wgn(s_i)
    #s_q_wgn = add_wgn(s_q)

    # Create and Save spectogram with LPI
    #filename = '{}_snr{}_{}'.format(args.mod, args.snr, i)
    #modulation.create_spectogram(s_i, s_q, modulation_vector, path + signals_without_noise_dir + filename)
    #modulation.create_spectogram(s_i_wgn, s_q_wgn, modulation_vector, path + signals_with_noise_dir + filename)

    # Create and save spectogram with only random noise
    #if args.noisy_samples:
        # Create and save random noise
        
    # Update metadata
    #metadata = metadata.append(some_data, ignore_index=True)
    #master_metadata = master_metadata.append(some_data, ignore_index=True)

# Save metadata files
metadata.to_csv(path+metadata_filename, index=False)
master_metadata.to_csv(data_dir+master_metadata_filename, index=False)

print("Done!")








