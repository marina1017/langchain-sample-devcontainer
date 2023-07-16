# Microsoftが提供するUbuntu Jammy（21.10）ベースの開発者向けコンテナイメージ
FROM mcr.microsoft.com/devcontainers/base:jammy

# ステートメントやログメッセージをKnativeのログに即座に表示できるようにする
ENV PYTHONUNBUFFERED True

# Debianパッケージマネージャであるaptがユーザーからのインタラクティブな入力を求めないようにするための環境変数を設定しています。
ARG DEBIAN_FRONTEND=noninteractive
# コンテナ内のユーザー名を指定
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \ 
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev

## Python and poetry installation ##
# コンテナ内で以降のコマンドを実行するユーザーを指定
USER $USER
# ユーザーのホームディレクトリを設定
ARG HOME="/home/$USER"
# インストールするPythonのバージョン
ARG PYTHON_VERSION=3.10

# 環境変数を設定
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

# PythonとPoetryをインストールしています
RUN echo "done 0" \
    && curl https://pyenv.run | bash \
    && echo "done 1" \
    && pyenv install ${PYTHON_VERSION} \
    && echo "done 2" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "done 3" \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

# poetoryで管理しているモジュールをインストール
COPY ./poetry.lock .
RUN poetry install --no-interaction --no-ansi