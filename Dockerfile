FROM python:3.10-slim-buster

ARG ENVIRONMENT
ARG USER_ID

ENV USERNAME blue
ENV ENVIRONMENT $ENVIRONMENT

ENV WORK_DIR /usr/src/app/
ENV REQUIREMENTS_DIR /usr/src/requirements
ENV CMD_DIR /usr/src/commands
ENV PATH=${PATH}:/home/${USERNAME}/.local/bin

# Cria um novo usuário (não root)
RUN groupadd --gid $USER_ID $USERNAME && \
    useradd --uid $USER_ID --gid $USER_ID -m $USERNAME

WORKDIR $WORK_DIR

# Cria os diretórios necessários para o COPY
RUN mkdir -p $REQUIREMENTS_DIR && mkdir -p $CMD_DIR

# Copia os arquivos/diretórios necessários para o container
COPY --chown=$USERNAME ./src/ $WORK_DIR
COPY --chown=$USERNAME ./requirements/${ENVIRONMENT}.txt ${REQUIREMENTS_DIR}/${ENVIRONMENT}.txt
COPY --chown=$USERNAME ./commands/${ENVIRONMENT}.sh ${CMD_DIR}/${ENVIRONMENT}.sh

# Define o usuário criado como default
USER $USERNAME

# Instalação de pacotes python
RUN pip install --user -r ${REQUIREMENTS_DIR}/${ENVIRONMENT}.txt

# Dá permissão de execução aos scripts
RUN chmod u+x ${CMD_DIR}/${ENVIRONMENT}.sh

# Define o script default do container
CMD ["sh", "-c", "bash ${CMD_DIR}/${ENVIRONMENT}.sh"]
