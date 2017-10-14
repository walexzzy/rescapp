#!/usr/bin/env python
# Rescapp main script
# Copyright (C) 2016, 2017 Adrian Gibanel Lopez
#
# Rescapp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rescapp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rescapp.  If not, see <http://www.gnu.org/licenses/>.

# 1st parametre = Partition device
# Returns True (Exit code 0) if filesystem can be shown. False (Exit code 2) if it is not found.

import parted
import _ped
import sys
import re

if ((len(sys.argv)-1) != 1 ):
        print 'Usage: ' + sys.argv[0] + ' ' + 'partition_device'
        print 'E.g.: ' + sys.argv[0] + ' ' + '/dev/sda2'
        sys.exit(1)

filesystem_partition_str=sys.argv[1]

filesystem_disk_str=re.sub(r'[0-9]*$', '', filesystem_partition_str)

filesystem_device = parted.Device(filesystem_disk_str,None)
filesystem_disk = parted.Disk(filesystem_device,None)
filesystem_partition = filesystem_disk.getPartitionByPath(filesystem_partition_str);



if (filesystem_partition.fileSystem is not None):
        filesystem_partition_type=filesystem_partition.fileSystem.type
        print filesystem_partition_type
        sys.exit(0)
else:
        sys.exit(2)


