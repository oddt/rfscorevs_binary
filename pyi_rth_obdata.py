#       Copyright 2011 Adrià Cereto Massagué <adrian.cereto@urv.cat>
#
#This is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2.1 of
# the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this software; if not, write to the Free
# Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA, or see the FSF site: http://www.fsf.org.

import sys

d = sys._MEIPASS

#Data files and plugins should be copied to sys._MEIPASS. OpenBabel plugins and data
#files are located in diferent places, depending on the platform.
#Copying all of them to the same directory is the easiest approach

os.environ["BABEL_DATADIR"] = os.path.join(d, 'data')
os.environ["BABEL_LIBDIR"] = d #Not nedded in Windows
os.environ["PATH"] = d + ";" + os.environ["PATH"] #Needed for Windows
