#! /bin/csh

foreach i ( */*.ram */*.rpm ) 
  echo $i
  sed 's"http://www.netfact.com"http://www-personal.umich.edu/~csev"' < $i > /tmp/crud
  cp /tmp/crud $i
end
