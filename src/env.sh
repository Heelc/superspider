PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env
PROJ_NAME=SUPERSPIDER

if [ ! -e ${VENV} ];then
    virtualenv --prompt "(${PROJ_NAME})" ${VENV} -p $(type -p python2.7)
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}/server:${PROJ_DIR}/modules:${PROJ_DIR}/draco:${PROJ_DIR}:$HOME/lib:${PROJ_DIR}/server/tasks

export PROJ_NAME
export PROJ_DIR


if [ -e ${HOME}/ora.env ];then
    source ${HOME}/ora.env
elif [ -e ora.env ];then
    source ora.env
fi
