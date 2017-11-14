from .tests.aws import encryption

class Console(object):
    @staticmethod
    def print_usage():
        print("Usage: terrascan SOURCE [OPTIONS]")

    @staticmethod
    def print_noargs():
        Console.print_usage()
        print("Missing arguments. Use 'terrascan --help' to see available options.")

    @staticmethod
    def print_help():
        Console.print_usage()
        print("Description: terrascan is a unit testing application that identifies security vulnerabilites in \
Terraform scripts.")
        print("")
        Console.print_help_options()
        print("")
        Console.print_unit_tests()

    @staticmethod
    def print_help_options():
        print("Options:")
        print("\t-T\tSet a group of tests to execute.")
        print("\t-t\tSet a specific test to execute.")

    @staticmethod
    def print_unit_tests():
        print("Unit Tests:")
        print("\tencryption")
        print("\t\t.aws_alb_listener_port")

        print("\t\t.aws_alb_listener_protocol")
        print("\t\t.aws_alb_listener_ssl_policy")

        print("\t\taws_alb_listener_certificate")

        print("\tlogging_and_monitoring")
        print("\t\t.alb_logging")
        print("\t\t.cloudtrail_logging")
        print("\t\t.cloudfront_distribution_logging")
        print("\t\t.elb_logging")
        print("\t\t.emr_cluster_logging")
        print("\t\t.kinesis_firehose_delivery_stream__s3_config_logging")
        print("\t\t.kinesis_firehose_delivery_stream_redshift_conf_logging")
        print("\t\t.kinesis_firehose_delivery_stream__es_config_logging")
        print("\t\t.redshift_cluster_logging")
        print("\t\t.s3_bucket_logging")
        print("\t\t.ssm_maintenance_window_task_logging")

    @staticmethod
    def print_tests(test_class):
        members = inspect.getmembers(encryption.TestAwsEncryption, predicate=inspect.isfunction)

        for member in members:
            if member[0][0:5] == "test_":
                print(member[0])
