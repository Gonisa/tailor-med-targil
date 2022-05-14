import logging
import configuration

logger = logging.getLogger('server_logger')
logging.basicConfig(filename=f"{configuration.ROOT_DIR}/logs.log", format='%(levelname)s - %(message)s',
                    level=logging.INFO)
