from ..test_group import TestGroup

class PublicExposureTestGroup(TestGroup):
    def test_alb_public(self):
        self.v.enable_variable_expansion()
        self.v.error_if_property_missing()
        self.v.resources(
            'aws_alb').property('internal').should_not_equal(False)

    def test_db_instance_public(self):
        self.v.enable_variable_expansion()
        self.v.resources(
            'aws_db_instance').property(
            'publicly_accessible').should_not_equal(True)

    def test_dms_replication_instance_public(self):
        self.v.enable_variable_expansion()
        self.v.error_if_property_missing()
        self.v.resources(
            'aws_dms_replication_instance').property(
            'publicly_accessible').should_not_equal(True)

    def test_elb_public(self):
        self.v.enable_variable_expansion()
        self.v.error_if_property_missing()
        self.v.resources(
            'aws_elb').property('internal').should_not_equal(False)

    def test_instance_public(self):
        self.v.enable_variable_expansion()
        self.v.resources(
            'aws_instance').property(
            'associate_public_ip_address').should_not_equal(True)

    def test_launch_configuration_public(self):
        self.v.enable_variable_expansion()
        self.v.resources(
            'aws_launch_configuration').property(
            'associate_public_ip_address').should_not_equal(True)

    def test_rds_cluster_instance_public(self):
        self.v.enable_variable_expansion()
        self.v.resources(
            'aws_rds_cluster_instance').property(
            'publicly_accessible').should_not_equal(True)

    def test_redshift_cluster_public(self):
        self.v.enable_variable_expansion()
        self.v.error_if_property_missing()
        self.v.resources(
            'aws_redshift_cluster').property(
            'publicly_accessible').should_not_equal(True)

    def test_s3_bucket_public(self):
        self.v.enable_variable_expansion()
        self.v.resources(
            'aws_s3_bucket').property(
            'acl').should_not_equal('public-read')
        self.v.resources(
            'aws_s3_bucket').property(
            'acl').should_not_equal('public-read-write')
        self.v.resources(
            'aws_s3_bucket').property(
            'acl').should_not_equal('authenticated-read')
        self.v.resources(
            'aws_s3_bucket').should_not_have_properties(
            ['website'])
